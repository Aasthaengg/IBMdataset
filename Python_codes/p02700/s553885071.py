a,b,c,d = map(int,input().split())
while a>0 and b>0:
  a-=d
  c-=b

if a <= 0 and c<=0:
  print('Yes')
elif c <= 0:
  print('Yes')
else:
  print('No')