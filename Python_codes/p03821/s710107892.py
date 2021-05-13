N = int(input())
A,B = [],[]
total = 0
for i in range(N):
    (a,b) = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(N):
    if (A[N-i-1]+total)%B[N-i-1] == 0:
        continue
    else:
        total += B[N-i-1]-((A[N-i-1]+total)%B[N-i-1])
print(total)