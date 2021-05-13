N,*L = map(int, open(0).read().split())
ls = [0]*N
for i,c in enumerate(zip(*[iter(L)]*2)):
  ls[i] = c
ls.sort()
pls = []
for i in range(N):
  for j in range(i+1,N):
    a,b = ls[i]
    x,y = ls[j]
    pls += [(x-a,y-b)]
ans = 10**10
for X,Y in pls:
  s = set()
  m = 0
  for x,y in ls:
    if (x-X, y-Y) not in s:
      m += 1
    s.add((x,y))
  ans = min(m,ans)
if N==1:
  ans = 1
print(ans)