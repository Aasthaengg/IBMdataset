N, T = map(int, input().split())
can = False
res = 1e5
for _ in range(N):
  c, t = map(int, input().split())
  if t <= T:
    can = True
    res = min(res, c)
print(res if can else "TLE")