n,m=map(int,input().split())
keys = []
A = [0]*m
for i in range(m):

    a,b=map(int,input().split())
    A[i] = a
    k = 0
    for c in map(int,input().split()):
        k = k| 2**(c-1)
        ## 鍵kがc番目の宝箱を開けられる--> k & 2**(c-1) == 1
    keys.append(k)



dp = [[10**9]*2**n for i in range(m+1)] #dp[i][j] iまで使って状態jを実現する最小コスト
dp[-1][0] = 0
for i in range(m):
    a = A[i]
    k = keys[i]
    for j in range(2**n):
        dp[i][j|k] = min(dp[i-1][j|k],dp[i-1][j]+a,dp[i][j|k])
        ## j|k -->jにkを使って開けられる宝箱の種類
        ## 前のまま(dp[i][j|k]) or jに鍵を使う(dp[i-1][j]+a)
        dp[i][j] = min(dp[i][j],dp[i-1][j]) # 鍵を使わない場合の更新
ans = dp[m-1][2**n-1]
if ans ==10**9:
    print(-1)
else:
    print(ans)
