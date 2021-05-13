n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
pos=[0]*n
s=0
for i in range(n):
  if b[i]-a[i]>=0:
    pos[i]=b[i]-a[i]
  else:
    s+=a[i]-b[i]
for p in pos:
  s-=p//2
if s<=0:
  print('Yes')
else:
  print('No')