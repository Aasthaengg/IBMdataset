import sys
input = sys.stdin.readline
H, W, M = map(int, input().split())
s = set()
ys = [0] * (H + 1)
xs = [0] * (W + 1)
for _ in range(M):
  y, x = map(int, input().split())
  s.add((y, x))
  ys[y] += 1
  xs[x] += 1

res = 0
mxy = []
mx = max(ys)
for i in range(H + 1):
  if ys[i] == mx: mxy.append(i)
res += mx

mxx = []
mx = max(xs)
for i in range(W + 1):
  if xs[i] == mx: mxx.append(i)
res += mx - 1

for x in mxx:
  for y in mxy:
    if (y, x) in s: continue
    res += 1
    break
  else: continue
  break
print(res)