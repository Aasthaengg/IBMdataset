def main():
  from collections import deque
  n,m=map(int,input().split())
  g=[[] for _ in range(n)]
  for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1;
    g[a].append((b,i))
    g[b].append((a,i))
  
  bfs=deque([])
  def check(j):
    res=1
    used=[False]*n
    used[0]=True
    bfs.append(0)
    while bfs:
      cur=bfs.popleft()
      for to,num in g[cur]:
        if num!=j and not used[to]:
          used[to]=True
          res+=1
          bfs.append(to)
    return res!=n
  
  ans=0
  for i in range(m):
    if check(i):
      ans+=1
  
  print(ans)
  
if __name__=='__main__':
  main()
