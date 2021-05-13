from collections import defaultdict
import sys
input = sys.stdin.readline
n,k,l = map(int,input().split())
road = [list(map(int,input().split())) for i in range(k)]
train = [list(map(int,input().split())) for i in range(l)]
rg = [[] for i in range(n+1)]
rv = [0 for i in range(n+1)]
tg = [[] for i in range(n+1)]
tv = [0 for i in range(n+1)]
def connect(road,rg,rv):
  for a,b in road:
    rg[a].append(b)
    rg[b].append(a)
  cnt = 0
  for i in range(1,n+1):
    if rv[i] == 0:
      cnt += 1
      stack = [i]
      while stack:
        x = stack.pop()
        rv[x] = cnt
        for y in rg[x]:
          if rv[y] == 0:
            stack.append(y)
            rv[y] = cnt
connect(road,rg,rv)
connect(train,tg,tv)
condc = defaultdict(list)
for i in range(1,n+1):
  cr = rv[i]
  ct = tv[i]
  condc[(cr,ct)].append(i)
ans = []
for i in range(1,n+1):
  cr = rv[i]
  ct = tv[i]
  ans.append(len(condc[(cr,ct)]))
print(*ans)