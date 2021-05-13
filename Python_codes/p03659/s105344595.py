N=int(input())
A=list(map(int, input().split()))
if N==2:
    print(abs(A[0]-A[1]))
    exit()
SUM=sum(A)
ans=float("INF")
now=0
for i in range(N-1):
    now+=A[i]
    ans=min(ans, abs(now-(SUM-now)))


print(ans)