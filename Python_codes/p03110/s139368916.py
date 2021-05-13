n = int(input())
total = 0
for _ in range(n):
  x, u = input().split()
  x = float(x)
  if u == 'JPY':
    total += x
  elif u == 'BTC':
    total += x * 380000.0
print(total)