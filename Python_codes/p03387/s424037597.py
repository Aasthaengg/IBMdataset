a=list(map(int,input().split()))
b=0
if a[0]==a[1]==a[2]:
  f=False
else:
  f=True
  
while f:
  if max(a)-min(a)>1:
    a.sort()
    a[0]+=2
    b+=1
  else:
    a.sort()
    a[0]+=1
    a[1]+=1
    b+=1
  if a[0]==a[1]==a[2]:
    f=False

print(b)