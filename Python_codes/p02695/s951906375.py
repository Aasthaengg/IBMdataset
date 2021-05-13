import itertools
n,m,q=map(int,input().split())
a=[]
for _ in range(q):
  b=list(map(int,input().split()))
  a.append(b)
  
g=list(range(1,m+1))
c=[]
for v in itertools.combinations_with_replacement(g,n):
  c.append(v)
  
ans1=[]
ans=0
for x in range(len(c)):
  d=c[x]
  ans1=0
  for r in range(q):
    a1=a[r][0]-1
    b1=a[r][1]-1
    c1=a[r][2]
    d1=a[r][3]
    if d[b1]-d[a1]==c1:
      ans1+=d1
      
  ans=max(ans,ans1)
  
print(ans)
    
    


