n,m = map(int, input().split())
t = [[n] for i in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  t[a-1].append(b-1)
g = []
for i in t:
  g.append(sorted(i))
k = 0
ans=0
while k <=n-1:
  e = n
  for i in g[k:]:
    e = min(e,i[0])
  if e==n:
    break
  ans+=1
  k = e
print(ans)