INF=float('inf')

N=int(input())
arr=list(map(int,input().split()))
A=[]
for i in range(N):
    A.append((arr[i],i))
A.sort(key=lambda x:x[0],reverse=True)
dp=[[-INF]*(N+1) for i in range(N+1)]
dp[0][0]=0

for i in range(N):
    a,w=A[i]
    for x in range(N+1):
        y=i-x+1
        if x>0:
            dp[i+1][x]=max(dp[i+1][x],dp[i][x-1]+a*abs(w-(x-1)))
        if y>=0:
            dp[i+1][x]=max(dp[i+1][x],dp[i][x]+a*abs(w-(N-y)))
print(max(dp[N]))