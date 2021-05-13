import sys

read=sys.stdin.read

n,m=map(int,input().split())
edge=[tuple(map(int,lst.split())) for lst in read().splitlines()]


def isconn(v,e0):
  clst=[1]*(n+1)
  clst[v]=0
  for _ in range(n):
    for e in edge:
      if e!=e0:
        tmp=clst[e[1]]&clst[e[0]]
        clst[e[1]]=tmp
        clst[e[0]]=tmp
  if sum(clst)>1:
    return False
  else:
    return True
ans=0
for e in edge:
  if not isconn(1,e):
    ans+=1
print(ans)