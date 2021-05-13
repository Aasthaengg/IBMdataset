n = int(input())
money = 0
for _ in range(n):
  p = input().split()
  if p[1] == 'JPY':
    money += int(p[0])
  elif p[1] == 'BTC':
    money += float(p[0]) * 380000

print(money)