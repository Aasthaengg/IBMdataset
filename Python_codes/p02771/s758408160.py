a,b,c=map(int,input().split())
d =0
if a==b:
  d+=1
if b==c:
  d+=1
if c==a:
  d+=1
if d==1:
  print('Yes')
else:
  print('No')