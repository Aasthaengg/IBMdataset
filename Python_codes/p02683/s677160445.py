def check(times):
  for i in range(m):
    if times[i] < x:
      return False
  else:
    return True

n, m, x = map(int, input().split())
c = [0] * n
a = [0] * n
for i in range(n):
  c[i], *a[i] = list(map(int, input().split()))
   
ans = 10**10
for i in range(2**n):
  times = [0] * m
  cnt = 0
  money = 0
  while i > 0:
    if i & 1:
      for j in range(m):
        times[j] += a[cnt][j]
      money += c[cnt]
    i = i >> 1
    cnt += 1
  if check(times):
    ans = min(money, ans)
if ans == 10**10:
  print(-1)
else:
  print(ans)