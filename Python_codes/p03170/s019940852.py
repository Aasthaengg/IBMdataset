n,k=map(int,input().split())
a=list(map(int,input().split()))
# dp[i]=石の個数が残り i 個の局面が勝ちか負けかを bool 値で表したもの
dp=[False]*(10**5+1)
dp[0]=False
for aa in a:
  dp[aa]=True

for i in range(1,k+1):
  ok=False
  for j in range(n):
    if i-a[j]>=0:
      if dp[i-a[j]]==0:
        ok=True
  if ok: 
    dp[i]=True
# print(dp[k])
print("First") if dp[k] else print("Second")
