H, N = map(int, input().split())
spells = []
for i in range(N):
  A, B = map(int, input().split())
  spells.append({"attack":A, "cost":B})

# O(HN)
dp = [0]
for i in range(H):
  dp.append(2147483648)
  
for h in range(H):
  for spell in spells:
    index = min(h+spell["attack"], H)
    current_min_mp = dp[index] 
    new_mp = dp[h] + spell["cost"]
    if (new_mp < current_min_mp):
      dp[index] = new_mp

print(dp[-1])