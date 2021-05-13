mod=1000000007
n,m=map(int,input().split())
S=tuple(map(int,input().split()))
T=tuple(map(int,input().split()))
DP=[[0]*(m+1) for _ in range(n+1)]
for i,s in enumerate(S):
    for j,t in enumerate(T):
        if s==t:
            DP[i+1][j+1]=DP[i][j+1]+DP[i+1][j]+1
        else:
            DP[i+1][j+1]=DP[i][j+1]+DP[i+1][j]-DP[i][j]
        DP[i+1][j+1]%=mod
print((DP[-1][-1]+1)%mod)