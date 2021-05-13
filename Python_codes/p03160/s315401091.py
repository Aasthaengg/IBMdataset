N=int(input())
H=list(map(int,input().split()))
dp=[float('inf')]*N
dp[0],dp[1]=0,abs(H[1]-H[0])

for i in range(2,N):
    x=dp[i-1]+abs(H[i]-H[i-1])
    y=dp[i-2]+abs(H[i]-H[i-2])
    dp[i]=min(x,y)

print(dp[N-1])