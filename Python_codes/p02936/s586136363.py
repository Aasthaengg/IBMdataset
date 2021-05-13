import sys
sys.setrecursionlimit(2*10**5+5)


def dfs(_v, _u):
  for u in v[_v]:
    if u==_u: continue;
    ans[u]+=ans[_v]
    dfs(u, _v)
        
  
def main():
  for i in range(n-1):
    a,b=map(lambda x:int(x)-1, input().split())
    v[a].append(b)
    v[b].append(a)
  
  for i in range(q):
    p,x=map(lambda x:int(x)-1, input().split())
    ans[p]+=x+1
  
  dfs(0,-1)
  
  print(*ans, sep=' ')
  
if __name__=='__main__':
  n,q=map(int,input().split())
  ans=[0]*n
  v=[[]*n for i in range(n)]
  main()