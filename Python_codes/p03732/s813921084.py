N, W = map(int, input().split())
d = {0:0}
for _ in range(N):
  w, v = map(int, input().split())
  for dw, dv in d.copy().items():
    if dw + w <= W:
      d[dw + w] = max(d.get(dw + w, 0), dv + v)
print(max(d.values()))