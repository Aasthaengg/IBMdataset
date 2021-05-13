a, b, c = map(int, input().split())
d = []
arr = []
for i in range(1, b + 1):
  d.append(i * a)
  arr.append((i * a) % b)
if c in arr:
  print('YES')
else:
  print('NO')