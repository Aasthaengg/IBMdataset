n,k=map(int,input().split())
a=list(map(int,input().split()))
k=bin(k)[2:]
p=[0]*40
for i,x in enumerate(a):
  for j in range(40):
    p[-1-j]+=(x>>j)&1
d=2**39
flag=1
b=0
for i in p[:-len(k)]:
  b+=i*d
  d//=2
ans=0
for i,x in enumerate(k):
  if x=='0':continue
  dy=d
  c=0
  for j,(y,z) in enumerate(zip(p[-len(k):],k)):
    if j<i:c+=[y,n-y][z=='1']*dy
    if j==i:c+=y*dy
    if j>i:c+=max(y,n-y)*dy
    dy//=2
  ans=max(ans,b+c)
c=0
for y,z in zip(p[-len(k):],k):
  c+=[y,n-y][z=='1']*d
  d//=2
print(max(ans,b+c))