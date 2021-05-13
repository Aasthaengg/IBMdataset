n,m = list(map(int,input().split()))

dp = [1e9 for _ in range(2**n)]
#dp[status]
# status : c1c2c3...を開けることができる=1としたときの2進⇒10進数(maxは1がnこ並ぶから2**n -1)
dp[0] = 0
for i in range(1,m+1):
  a, _ = list(map(int,input().split()))
  C = list(map(int,input().split()))
  s = sum([2**(c-1) for c in C]) ## 内包forできれいに書いてる
  for j in range(2**n): ## ひとつ前のステータスを総当たりでいく
    dp[j|s] = min(dp[j|s], dp[j] + a)  ## このorの書き方が美しいのか

ans = dp[2**n-1] # 全部のカギを使ったときのstatusがすべて1の時
print(ans if ans < 1e9 else -1)