N,T = map(int,input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())

# T-1分以内に完食を目指す，特定の料理のみ使わないで計算したい．
#DP1[i][t]はi番目の料理まででt分後までに完食で得られる幸福度の最大(商品番号は1から振る)
#DP2[i][t]はiからN番目の料理でt分後までに完食で得られる幸福度の最大

dp1 =[[0]*T for _ in range(N+1)]
dp2 =[[0]*T for _ in range(N+1)]

for i in range(N):
    for t in range(1,T):
        dp1[i+1][t] = dp1[i][t]
        if t-A[i]>=0:
            dp1[i+1][t]=max(dp1[i][t],dp1[i][t-A[i]]+B[i])


for i in reversed(range(0,N)):
    for t in range(1,T):
        dp2[i][t] = dp2[i+1][t]
        if t-A[i]>=0:
            dp2[i][t]=max(dp2[i+1][t],dp2[i+1][t-A[i]]+B[i])


ans=0
#i番目の料理を時間ギリギリに注文
for i in range(1,N):
    for j in range(0,T):
        ans = max(ans,dp1[i][j]+dp2[i+1][T-1-j]+B[i])
print(ans)