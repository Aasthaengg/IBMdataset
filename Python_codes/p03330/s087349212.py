n,c = map(int,input().split())
d = [[int(i) for i in input().split()] for _ in range(c)]
lc = [[int(i)-1 for i in input().split()] for _ in range(n)]

ans = float("inf")

dp = [[0] * c for i in range(3)]
for C in range(c):
  for y in range(n):
    for x in range(n):
      if lc[y][x] != c:
        dp[(y+x)%3][C] += d[lc[y][x]][C]
for c0 in range(c):
  for c1 in range(c):
    if c0 == c1: continue
    for c2 in range(c):
      if c0 == c2 or c1 == c2: continue
      ans = min(ans, dp[0][c0] + dp[1][c1] + dp[2][c2])
print(ans)
