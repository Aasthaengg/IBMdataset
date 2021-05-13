N, S = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
dp = [-1 for _ in range(S+1)]
visited = [0]
dp[0] = 1
dp = tuple(dp)
for k in range(N):
  a = A[k]
  nextdp = list(dp)
  nextvisit = []
  for item in visited:
    #process1 追加する
    if item + a <= S:
      if nextdp[item+a] == -1:
        nextvisit.append(item+a)
        nextdp[item+a] = 0
      nextdp[item+a] += dp[item]
      nextdp[item+a] %= mod
    #process2 追加しない
    nextdp[item] += dp[item]
    nextdp[item] %= mod
  dp = tuple(nextdp)
  visited.extend(nextvisit)

print(max(dp[-1], 0))
