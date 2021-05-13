n=int(input())
a=list(map(int,input().split()))
al=0
for i in range(n):
  if a[i]>=3200:
    al+=1
    a[i]=8
  else:
    a[i]=a[i]//400
if al==0:
  cl=len(set(a))
else:
  cl=len(set(a))-1
if cl==0:
  mi=1
else:
  mi=cl
ma=al+cl
print(mi,ma)