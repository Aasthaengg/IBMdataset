n, m = map(int, input().split())
ks = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
  onswichi = [False] * n
  onlight = [0] * m
  for j in range(n):
    if (i >> j) & 1:
      onswichi[j] = True
  for k in range(m):
    cnt = 0
    for f in ks[k][1:]:
      if onswichi[f-1]:
        cnt += 1
    if cnt % 2 == p[k]:
      onlight[k] = 1
  if sum(onlight) == m:
    ans += 1
print(ans)