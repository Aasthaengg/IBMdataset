import sys
import numpy as np
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**5)

def dfs(s):
  for u in to[s]:
    if not toflag[u]:
      toflag[u]=True
      dfs(u)

def rdfs(s):
  for u in ot[s]:
    if not otflag[u]:
      otflag[u]=True
      rdfs(u)

def main():
  for i in range(m):
    a,b,c=map(lambda x:int(x)-1, input().split())
    edges[i]=[a,b,-(c+1-p)]
    to[a].append(b)
    ot[b].append(a)
  
  toflag[0]=True
  otflag[-1]=True
  dfs(0)
  rdfs(n-1)
  
  dic={}
  for a,b,c in edges:
    if toflag[a] and otflag[b]:
      if (a,b) in dic.keys():
        dic[(a,b)]=min(dic[(a,b)],c)
      else:
        dic[(a,b)]=c
        
  row=[]
  col=[]
  data=[]
  for (a,b),c in dic.items():
      row.append(a)
      col.append(b)
      data.append(c)
  g=csr_matrix((data,(row,col)), shape=(n,n))
  try:
    d=bellman_ford(g,indices=0).astype(int)
    print(max(0,-d[-1]))
  except NegativeCycleError:
    print(-1)

    
if __name__=='__main__':
  n,m,p=map(int,input().split())
  edges=[[] for i in range(m)]
  to=[[] for i in range(n)]
  ot=[[] for i in range(n)]
  toflag=[False]*n
  otflag=[False]*n
  main()