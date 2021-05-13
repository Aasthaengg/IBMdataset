x = int(input())
amount = 100
res = 0
while amount < x:
  amount += amount // 100
  res += 1

print(res)