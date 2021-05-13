from collections import deque
H, W, D = map(int, input().split())
mod_dict = [deque() for _ in range(D)]
h = 0
while h < H:
  A = list(map(int, input().split()))
  w = 0
  while w < W:
    a = A[w]
    mod_dict[a%D].append((a, h, w))
    w += 1
  h += 1
ruiseki_dict = [deque() for _ in range(D)]
d = 0
while d < D:
  m = sorted(mod_dict[d], key=lambda x:x[0])
  py, px = m[0][1], m[0][2]
  ruiseki_dict[d].append(0)
  i = 0 if d == 0 else 1
  while i < len(m):
    ry, rx = m[i][1], m[i][2]
    ruiseki_dict[d].append(ruiseki_dict[d][-1]+abs(ry-py)+abs(rx-px))
    py, px = ry, rx
    i += 1
  d += 1
Q = int(input())
for _ in range(Q):
  l, r = list(map(int, input().split()))
  d = ruiseki_dict[r%D]
  print(d[r//D]-d[l//D])