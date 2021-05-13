import bisect
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))[::-1]
b=sorted(list(map(int,input().split())))
ma=a[0]*b[-1]
mi=0
if sum(a)<k+1:
  ma=0
for i in range(n):
  a[i]=a[i]*b[i]
while abs(ma-mi)>1:
  now=0
  for i in range(n):
    now+=max(0,(a[i]-(mi+ma)//2+b[i]-1)//b[i])
  if now>k:
    mi=(ma+mi)//2
  else:
    ma=(ma+mi)//2
print(ma)