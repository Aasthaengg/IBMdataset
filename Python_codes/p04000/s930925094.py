from collections import defaultdict
H, W, N = map(int, input().split())
P = [0] * 10
P[0] = (H - 2) * (W - 2)
G = defaultdict(lambda: defaultdict(int))
for i in range(N):
  a, b = map(int, input().split())
  for i in range(max(a - 3, 0), min(a, H - 2)):
    for j in range(max(b - 3, 0), min(b, W - 2)):
      p = G[i][j]
      P[p] -= 1
      P[p + 1] += 1
      G[i][j] += 1
for i in range(10):
  print(P[i])