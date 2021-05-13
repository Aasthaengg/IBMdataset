from collections import defaultdict, Counter

H, W, N = map(int, input().split())

D = defaultdict(int)

for _ in range(N):
  a, b = map(int, input().split())
  for i in range(a - 2, a + 1):
    if 1 <= i <= H - 2:
      for j in range(b - 2, b + 1):
        if 1 <= j <= W - 2:
          D[(i, j)] += 1

print((H - 2) * (W - 2) - len(D))

c = Counter(D.values())
for i in range(1, 10):
  print(c.get(i, 0))