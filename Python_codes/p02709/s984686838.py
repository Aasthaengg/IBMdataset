from operator import itemgetter
N=int(input())
A=list(map(int, input().split()))
B=[[i, A[i]] for i in range(N)] 
B=sorted(B, key=itemgetter(1), reverse=True)

dp=[[0]*(N+1) for _ in range(N+1)]

for x in range(N):
    dp[x+1][0]=dp[x][0]+B[x][1]*abs(B[x][0]-x)
    
for y in range(N):
    dp[0][y+1]=dp[0][y]+B[y][1]*abs(N-1-y-B[y][0])
    
for z in range(2, N+1):
    for x in range(1, z):
        y=z-x
        dp[x][y]=max(dp[x][y-1]+B[z-1][1]*abs(N-y-B[z-1][0]), dp[x-1][y]+B[z-1][1]*abs(x-1-B[z-1][0]))
        
print(max([dp[x][N-x] for x in range(N+1)]))