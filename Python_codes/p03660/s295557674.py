import sys
sys.setrecursionlimit(1000000)
N=int(input())
ab=[[] for _ in range(N)]
for _ in range(N-1):
  a,b=map(int,input().split())
  ab[a-1].append(b)
  ab[b-1].append(a)
"""
N=10**5
ab=[[]]*N
ab[0]=[2]
ab[N-1]=[N-1]
for i in range(1,N-1):
  ab[i]=[i,i+2]
"""
par=[0]*N
  
def dfs(pre,p):
  global path
  par[p-1]=pre
  if p==N:
    pass
  else:
    for i in ab[p-1]:
      if i!=pre:
        dfs(p,i)

dfs(-1,1)
path=[N]
p=N
while p!=1:
  p=par[p-1]
  path.append(p)
path.reverse()

spath=set(path)

def dfs2(pre,p):
  a=0
  for i in ab[p-1]:
    if i in spath:
      pass
    elif i==pre:
      pass
    else:
      a+=dfs2(p,i)
  return 1+a

ff=0
sf=0
L=len(path)
for i in range(L):
  if i<=(L-1)//2:
    ff+=dfs2(-1,path[i])
  else:
    sf+=dfs2(-1,path[i])
    
if ff>sf:
  print("Fennec")
else:
  print("Snuke")
