L=[]
def make_list(n,m,p,l):
  if n==0:
    L.append(l)
  else:
    for i in range(p,m+1):
      make_list(n-1,m,i,l+[i])
  
N,M,Q = map(int,input().split())
T=[tuple(map(int,input().split())) for _ in range(Q)]
ans=0
make_list(N,M,1,[])
for l in L:
  tmp=0
  for a,b,c,d in T:
    if l[b-1]-l[a-1]==c:
      tmp+=d
  ans=max(ans,tmp)
print(ans)