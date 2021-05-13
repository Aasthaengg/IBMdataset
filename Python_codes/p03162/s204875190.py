n=int(input())
active_list=[list(map(int,input().split())) for _ in range(n)]
dp=[[0,0,0] for _ in range(n)]
for i in range(3):
    dp[0][i]=active_list[0][i]
for j in range(n-1):
    for k in range(3):
        dp[j+1][k]=max(dp[j][k-1]+active_list[j+1][k],dp[j][k-2]+active_list[j+1][k])
print(max(dp[-1]))
