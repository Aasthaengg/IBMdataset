from collections import defaultdict as dd
H, W, N = map(int, input().split())
res = [0] * 10
res[0] = H * W - 2 * H - 2 * W + 4
p = dd(int)
d = [-1, 0, 1]
for _ in range(N):
  y, x = map(int, input().split())
  for i in d:
    for j in d:
      if 1 < y + i < H and 1 < x + j < W:
        p[(y + i) * (H * W + 1) + x + j] += 1
for k in p.keys():
  res[p[k]] += 1
  res[0] -= 1
for r in res:
  print(r)