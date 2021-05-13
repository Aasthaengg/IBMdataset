N = int(input())
A = list(map(int, input().split()))

A.sort()

cum = [A[0]]
for i in range(1,N):
    cum.append(cum[-1]+A[i])

for i in reversed(range(N-1)):
    if cum[i] * 2 >= A[i+1]:
        continue
    else:
        print(N-1-i)
        break
else:
    print(N)