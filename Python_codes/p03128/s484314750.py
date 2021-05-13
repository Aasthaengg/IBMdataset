n, m = map(int, input().split())
a = list(map(int, input().split()))
 
needs = [999,2,5,5,4,5,6,3,7,6]

dp=[-1]*(n+10) #needsを探索できるようにするため
dp[0]=0

for i in range(n): #小さい桁数から全探索する
  if dp[i]!=-1:
    for k in sorted(a, reverse=True): #aのうち大きい数字から試す
      matchs = needs[k] #必要なマッチの本数
      dp[i+matchs] = max(dp[i+matchs], dp[i]*10+k) #dpからの遷移
print(dp[n])