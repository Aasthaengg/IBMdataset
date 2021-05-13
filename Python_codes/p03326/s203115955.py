N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(2**3):
  coeff = []
  for j in range(3):
    coeff.append([1, -1][i>>j & 1])
  cakes = []
  for v in xyz:
    cakes.append([sum(map(lambda x:x[0]*x[1], zip(coeff, v)))]+v)
  cakes.sort(reverse=True)
  val = [0, 0, 0]
  for m in range(M):
    for j in range(3):
      val[j] += cakes[m][j+1]
  ans = max(ans, sum(map(abs, val)))

print(ans)