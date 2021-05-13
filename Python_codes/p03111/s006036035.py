n,a,b,c=map(int,input().split())
l=[int(input()) for _ in range(n)]
def func(g):
  if len(g[0])==0 or len(g[1])==0 or len(g[2])==0:return -1
  ret=0
  ret+=10*(len(g[0])-1)
  ret+=10*(len(g[1])-1)
  ret+=10*(len(g[2])-1)
  a_=sum([l[i] for i in g[0]])
  b_=sum([l[i] for i in g[1]])
  c_=sum([l[i] for i in g[2]])
  ret+=abs(a-a_)
  ret+=abs(b-b_)
  ret+=abs(c-c_)
  return ret
m=n*2
ans=pow(10,9)
for i in range(2**m):
  g=[[]for _ in range(4)]
  for j in range(n):
    g[(i//pow(4,j))%4].append(j)
  tmp=func(g)
  if tmp>=0:
    ans=min(ans,tmp)

print(ans)
