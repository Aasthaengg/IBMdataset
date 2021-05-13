n,t=map(int,input().split())
a=list(map(int,input().split()))
b=c=0
m=a[0]
for i in range(n):
  if a[i]<m:
    m=a[i]
    continue
    
  d=a[i]-m
  if b<d:
    b=d
    c=1
  elif b==d:
    c+=1
print(c)