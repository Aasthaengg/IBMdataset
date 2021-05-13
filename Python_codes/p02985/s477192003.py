N,K=map(int,input().split())
mod=1000000007
path=[[] for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  path[a].append(b)
  path[b].append(a)
#print(path)
  
abc=[False for i in range(N)] #0ならまだ塗ってない
 
abc[0]=True
cnt=0
ans=K%mod
nx=[]
for i in range(len(path[0])):
  child=path[0][i]
  if abc[child]:
    continue
  ans=ans*(K-1-cnt)
  ans=ans%mod
  cnt=cnt+1
  abc[child]=True
  nx.append(child)
while len(nx)>0:
  a=nx.pop()
  cnt=0
  for i in range(len(path[a])):
    child=path[a][i]
    if abc[child]:
      continue
    ans=ans*(K-2-cnt)
    ans=ans%mod
    cnt=cnt+1
    abc[child]=True
    nx.append(child)
      
print(ans%mod)