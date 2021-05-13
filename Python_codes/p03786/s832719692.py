N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
sums = [0]

for i in range(N-1):
    sums.append(sums[-1] + A[i])

sums = list(reversed(sums))
A = list(reversed(A))

ans = 1
flag = True
for i in range(N):
    if sums[i] * 2 >= A[i] and flag:
        ans += 1
    else:
        flag = False

print(ans)
