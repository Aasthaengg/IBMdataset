n,m=map(int,input().split())
p=[]
pp=[]
for i in range(1,int(m**0.5)+1):
  if m%i==0:
    p.append(i)
    pp.append(m//i)
pp.reverse()
p+=pp
l,r=-1,len(p)
while r-l!=1:
  t=(l+r)//2
  if p[t]>=n:
    r=t
  else:
    l=t
print(m//p[r])