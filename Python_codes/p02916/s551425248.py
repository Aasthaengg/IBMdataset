a=int(input())
Order = list(map(int, input().split()))
Happiness = list(map(int, input().split()))
Bonus = list(map(int, input().split()))
res = 0
mae = -1
for i in Order:
  res += Happiness[i-1]
  if mae == -1:
    pass
  elif mae == i-1:
    res += Bonus[i-2]
  mae = i
print(res)