#解説参照
n,m = map(int, input().split( ))
a = list(map(int, input().split( )))
mch = (100,2,5,5,4,5,6,3,7,6)

dp = [-1]*(n+10)
dp[0] = 0
for i in range(n+1):##nまでなので+1
    for aj in a:
        if dp[i-mch[aj]]>=0:##ちょうどn本使う必要がある
            dp[i] = max(dp[i], dp[i-mch[aj]]*10+aj)
print(dp[n])
