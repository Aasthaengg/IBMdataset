pxcount=0
pycount=0
pzcount=0

n=int(input())
a,b=map(int, input().split())
p=list(map(int, input().split()))

for i in p:
  if i<=a:
    pxcount=pxcount+1
for i in p:
  if a+1<=i and i<=b:
    pycount=pycount+1
for i in p:
  if b+1<=i:
    pzcount=pzcount+1
  
print(min(pxcount,pycount,pzcount))