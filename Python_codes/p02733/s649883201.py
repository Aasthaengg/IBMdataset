from itertools import combinations

H, W, K = map(int, input().split())

map = [None] * H
for i in range(H):
  map[i] = [int(c) for c in input().strip()]


def a(heights=[]) -> int:
  assert len(heights) > 0
  count = len(heights) - 1

  total = {i: (0, 0) for i in range(len(heights))}
  for i in range(W):
    violate = False
    for j, height in enumerate(heights):
      n = 0
      for k in range(height[0], height[1]):
        n += map[k][i]
      if n > K:
        return -1
      total[j] = (total[j][0] + n, n)
      if total[j][0] > K:
        violate = True
    if violate:
      count += 1
      for j in range(len(heights)):
        tmp = total[j][1]
        total[j] = (tmp, tmp)
  return count


patterns = [[(0, H)]]
iterable = [i + 1 for i in range(H - 1)]
for r in range(1, H):
  for c in combinations(iterable, r):
    pattern = []
    last = 0
    for i in c:
      pattern.append((last, i))
      last = i
    pattern.append((last, H))
    patterns.append(pattern)

print(min(filter(lambda x: x >= 0, [a(p) for p in patterns])))
