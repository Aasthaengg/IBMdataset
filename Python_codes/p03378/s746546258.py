N,M,X = map(int,input().split())
A = list(map(int,input().split()))

masu = [0]*(N+1)
for i in range(M):
    masu[A[i]]=1

ans = min(sum(masu[0:X]),sum(masu[X:N+1]))
print(ans)