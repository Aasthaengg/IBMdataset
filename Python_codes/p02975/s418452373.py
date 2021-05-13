n=int(input())
a=list(map(int,input().split()))
x='No'
p=len(set(a))
if p==1:
  if a[0]==0:
    x='Yes'
elif p==2:
  if n%3==0:
    if a.count(0)==n//3:
      x='Yes'
elif p==3:
  if n%3==0:
    b=set(a)
    t=0
    f=1
    for i in b:
      t=t^i
      if a.count(i)!=n//3:
        f=0
    if t==0 and f:
      x='Yes'
print(x)