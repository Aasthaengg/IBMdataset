from bisect import bisect_right


a, b, q = map(int, input().split())
INF = 10 ** 18
J = [-INF] + [int(input()) for _ in range(a)] + [INF]
T = [-INF] + [int(input()) for _ in range(b)] + [INF]

for _ in range(q):
  s = int(input())
  b, d = bisect_right(J, s), bisect_right(T, s)
  res = INF
  for j in [J[b - 1], J[b]]:
    for t in [T[d - 1], T[d]]:
      d1, d2 = abs(j - s) + abs(t - j), abs(t - s) + abs(j - t)
      res = min(res, d1, d2)
  print(res)