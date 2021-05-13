def dist(x,y):
  return abs(x[0]-y[0])+abs(x[1]-y[1])

n,m = map(int,input().split())
s = []
for _ in range(n):
  a,b = map(int,input().split())
  s.append((a,b))
c = []
for _ in range(m):
  c_,d = map(int,input().split())
  c.append((c_,d))
for i in range(n):
  p = s[i]
  md = 10**10
  mi = 0
  for j in range(m):
    ch = c[j]
    d = dist(p,ch)
    if md > d:
      md = d
      mi = j
  print(mi+1)