N,*ABC=map(int,input().split())
M=3
ans=10**9
L=[]
for i in range(N):
  l=int(input())
  if l in ABC:
    ABC.remove(l)
    N-=1
    M-=1
  else:
    L.append(l)
if M==0:
  print(0)
  exit(0)
for x in range((M+1)**N):
  _=0
  abc=[0]*(M+1)
  for i in range(N):
    if x%(M+1)!=M and abc[x%(M+1)]>0:
      abc[x%(M+1)]+=L[i]
      _+=10
    else:
      abc[x%(M+1)]+=L[i]
    x=x//(M+1)
  if min(abc[:M])==0:
    continue
  for i in range(M):
    _+=abs(ABC[i]-abc[i])
  ans=min(ans,_)
  
print(ans)