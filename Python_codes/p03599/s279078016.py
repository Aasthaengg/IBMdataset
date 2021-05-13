import sys
readline = sys.stdin.readline

# 作れる水の量を全探索（せいぜい30種類）
# 各水の量に対して、溶かせる砂糖の最大値は決まる（DPする）
# 最大値とすることができる砂糖に最も近づいたら割合を求め、答えの最大値を更新する

A,B,C,D,E,F = map(int,readline().split())
max_rate = -1
ans_water = 0
ans_sugar = 0
for a in range(30):
  for b in range(30):
    if a * A * 100 + b * B * 100 >= F:
      continue
    water = a * A * 100 + b * B * 100
    if water == 0:
      continue
    max_sugar = water * E // 100 # 溶ける砂糖の最大値
    if max_sugar + water > F:
      max_sugar = F - water
      
    dp = [False] * (max_sugar + 1)
    dp[0] = True
    for i in range(len(dp)):
      if dp[i]:
        if i + C >= len(dp):
          break
        dp[i + C] = True
    
    for i in range(len(dp)):
      if dp[i]:
        if i + D >= len(dp):
          break
        dp[i + D] = True
        
    for i in range(len(dp) - 1, -1, -1):
      if dp[i]:
        rate = (i * 100) / (water + i)
        break
    if rate >= max_rate:
      max_rate = rate
      ans_water = water
      ans_sugar = i
    
print(ans_water + ans_sugar,ans_sugar)