import itertools
h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
s = []
for i, j in itertools.product(range(h), range(w - 1)):
  if a[i][j] % 2 == 1:
    s.append((i + 1, j + 1, i + 1, j + 2))
    a[i][j] -= 1
    a[i][j + 1] += 1
for i in range(h - 1):
  if a[i][w - 1] % 2 == 1:
    s.append((i + 1, w, i + 2, w))
    a[i][w - 1] -= 1
    a[i + 1][w - 1] += 1
print(len(s))
for l in s:
  print(*l)
