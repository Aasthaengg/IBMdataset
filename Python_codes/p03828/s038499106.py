n = int(input())
dp = list(0 for _ in range(n+1))

for i in range(2,n+1):
  #素因数分解の試し割り法
  while i%2==0:
    dp[2] += 1
    i //= 2
  f = 3
  while f*f<=i:
    if i%f==0:
      dp[f] +=1
      i //= f
    else:
      f += 2
  if i!=1:
    dp[i] += 1
#指数を数えていく
s = 1
for i in dp:
  if i!=0:
    s *= i+1
print(s%(10**9+7))