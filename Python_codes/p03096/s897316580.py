import sys
input = sys.stdin.readline
N=int(input())
mod=10**9+7
C=[int(input()) for i in range(N)]
M=max(C)+2
dp=[0]*(N+1)
co=[0]*M
co[C[0]]=1
for i in range(1,N+1):
    if i<N and C[i-1]==C[i]:
        continue
    dp[i]+=co[C[i-1]]
    if i<N:
        co[C[i]]+=dp[i]
        co[C[i]]%=mod
    #print(dp,co)
print(dp[-1])
