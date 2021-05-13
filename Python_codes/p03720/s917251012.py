n, m = map(int, input().split())
a, b = [], []
for i in range(m):
  p, q = map(int, input().split())
  a.append(p)
  b.append(q)

for i in range(n):
  print(a.count(i + 1) + b.count(i + 1))