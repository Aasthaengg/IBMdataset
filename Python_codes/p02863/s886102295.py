#Aをソートしておく，時間ギリギリにi番目の料理を頼むことで固定．
N,T = map(int,input().split())
AB = [[0,0] for _ in range(N)]

for i in range(N):
    AB[i][0],AB[i][1] = map(int,input().split())

AB.sort()
#ソートした時のbの情報を維持しないと

# T-1分以内にi番目以外の料理をできるだけ完食する
#DP1[i][t]はi番目の料理まででt分後までに完食で得られる幸福度の最大(商品番号は1から振る)


dp1 =[[0]*T for _ in range(N+1)]

for i in range(N):
    for t in range(1,T):
        dp1[i+1][t] = dp1[i][t]
        if t-AB[i][0]>=0:
            dp1[i+1][t]=max(dp1[i][t],dp1[i][t-AB[i][0]]+AB[i][1])
            
ans=0
for i in range(N):
    ans=max(ans,dp1[i][-1]+AB[i][1])
print(ans)