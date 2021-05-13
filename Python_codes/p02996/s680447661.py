n=int(input())
a=[]
for _ in range(n):
  b=list(map(int,input().split()))
  a.append(b)
  
a.sort(key=lambda x: x[1])

ans=0
ch=0

for c in range(n):
  x=a[c][0]
  y=a[c][1]
  
  ans+=x
  if ans>y:
    ch+=1
  
if ch==0:
  print('Yes')
else:
  print('No')