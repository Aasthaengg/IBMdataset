n, t = map(int, input().split())
ct = [list(map(int, input().split())) for i in range(n)]
ans = 10 ** 10
cnt = 0
for i in range(n):
  if ct[i][1] <= t:
    ans = min(ans, ct[i][0])
    cnt += 1
if cnt > 0:
  print(ans)
else:
  print("TLE")