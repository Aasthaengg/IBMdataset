from bisect import bisect_left
N=int(input())
C=[int(input()) for i in range(N)]
mod=10**9+7
data=[[] for i in range(max(C)+1)]
for i in range(N):
    data[C[i]].append(i)
dp=[0]*N
dp[0]=1
for i in range(1,N):
    h=data[C[i]]
    b=bisect_left(h,i)
    if b==0:
        dp[i]=dp[i-1]
    elif C[i]==C[i-1]:
        dp[i]=dp[i-1]
    else:
        dp[i]=(dp[i-1]+dp[h[b-1]])%mod
print(dp[-1]%mod)