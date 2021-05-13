a,b,c=map(int,input().split())
d=max(a,b,c)
if d==a:
  if d==b+c:
    print('Yes')
  else:
    print('No')
elif d==b:
  if d==a+c:
    print('Yes')
  else:
    print('No')
elif d==c:
  if d==a+b:
    print('Yes')
  else :
    print('No')