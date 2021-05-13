n,m=map(int,input().split())
p=list(map(int,input().split()))
xs=[tuple(map(int,input().split())) for _ in range(m)]
def root(n):
  if union[n]==n:
    return n
  union[n]=root(union[n])
  return union[n]
union={x:x for x in range(1,n+1)}
for x,y in xs:
  union[root(x)]=root(y) 
print(sum(root(i+1)==root(p[i]) for i in range(n)))