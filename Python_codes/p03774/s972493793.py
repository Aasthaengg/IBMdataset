n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
  res = []
  ans = []
  for j in range(m):
    res.append(abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]))
  ans = res.index(min(res))
  print(ans+1)