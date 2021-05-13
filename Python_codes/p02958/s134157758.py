n, p = int(input()), list(map(int, input().split()))
px = sorted(p)
a = 0
for i in range(n):
  if p[i] != px[i]:
    a += 1
if a/2 <= 1:
  print('YES')
else:
  print('NO')