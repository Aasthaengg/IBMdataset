n,c,k = map(int, input().split())
t = [int(input()) for i in range(n)]
t.sort()

bus = 0
vis = [False for i in range(n)]
for i in range(n):
  if vis[i]:
    continue
  vis[i] = True
  x = i
  lim = t[i]+k
  cnt = 1
  bus += 1
  while x < n and cnt <= c:
    if t[x] > lim:
      break
    i = x
    vis[x] = True
    x += 1
    cnt += 1
print (bus)
