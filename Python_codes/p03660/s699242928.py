import sys
input = sys.stdin.readline
import copy
n = int(input())
ab = [list(map(int,input().split())) for _ in range(n-1)]
point = [[] for _ in range(n+1)]
for l in ab:
  point[l[0]].append(l[1])
  point[l[1]].append(l[0])
adone = set()
bdone = set()
adone.add(1)
bdone.add(n)
da,db = [0]*(n+1),[0]*(n+1)
alist = [1]
blist = [n]
anext,bnext = [],[]
c = 0
while alist:
  c += 1
  for i in alist:
    for j in point[i]:
      if j not in adone:
        adone.add(j)
        anext.append(j)
        da[j] = c
  alist = copy.deepcopy(anext)
  anext = []
c = 0
while blist:
  c += 1
  for i in blist:
    for j in point[i]:
      if j not in bdone:
        bdone.add(j)
        bnext.append(j)
        db[j] = c
  blist = copy.deepcopy(bnext)
  bnext = []
a,b = 0,0
for i in range(1,n+1):
  if da[i] <= db[i]:
    a += 1
  else:
    b += 1
if a > b:
  print("Fennec")
else:
  print("Snuke")