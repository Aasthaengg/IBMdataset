import itertools
h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
p = [0] * (h * w)
for i, j in itertools.product(range(h), range(w)):
  p[a[i][j] - 1] = (i, j)
s = [0] * d
for i in range(h * w - d):
  s.append(s[-d] + abs(p[i][0] - p[i+d][0]) + abs(p[i][1] - p[i+d][1]))
q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  l -= 1
  r -= 1
  print(s[r] - s[l])
