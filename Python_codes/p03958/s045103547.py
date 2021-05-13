K, T = map(int, input().split())
numbers = [int(x) for x in input().split()]

table = [False] * (K + 1)

table[0] = True

for n in numbers:
  for i in range(K, 0, -1):
    if i - n >= 0:
      table[i] = table[i] or table[i - n]
    
m = 0

for i, t in enumerate(table):
  if not t:
    continue
  m = i if abs(i - K / 2) < abs(m - K / 2) else m

if abs(2 * m - K) <= 1:
  print(0)
else:
  print(abs(2 * m - K) - 1)