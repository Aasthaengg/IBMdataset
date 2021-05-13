n,m = map(int,input().split())
a = list(map(lambda z:int(z)-1,input().split()))
pre = [i for i in range(n)]
for _ in range(m):
  x,y = map(lambda z:int(z)-1,input().split())
  while pre[x] != x:
    x = pre[x]
  while pre[y] != y:
    y = pre[y]
  if x == y:
    continue
  elif x < y:
    pre[y] = x
  else:
    pre[x] = y
home1 = [10**6 for _ in range(n)]
home2 = [10**6 for _ in range(n)]
for i in range(n):
  I = i
  while pre[I] != I:
    I = pre[I]
  home1[i] = I
  home2[a[i]] = I
ans = 0
for i in range(n):
  if home1[i] == home2[i]:
    ans += 1
print(ans)