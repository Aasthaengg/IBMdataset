n=int(input())
l=[]
m=[]
for i in range(0,n):
  a,b=map(int,input().split())
  l.append(a)
  m.append(b)
c=0
i=0
while i<=n-3:
  if l[i]==m[i] and l[i+1]==m[i+1] and l[i+2]==m[i+2]:
      c=3
  i=i+1
if c==3:
  print('Yes')
else:
  print('No')
