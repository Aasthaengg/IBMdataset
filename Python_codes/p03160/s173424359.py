N=int(input())
h=list(map(int,input().split()))
# N = 4
# h = [10, 30, 40, 20]
dp = [1000000]*N
#d[i]はカエルが足場iへと移動するのに必要な最小コスト
dp[0]=0
for i in range(1,N):
    if i == 1:
        dp[i] = dp[i-1]+abs(h[i]-h[i-1])
    else:
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
# print(dp)
# print("min cost=",dp[-1])
print(dp[-1])