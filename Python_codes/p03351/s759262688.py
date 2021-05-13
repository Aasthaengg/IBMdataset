a,b,c,d=map(int,input().split())
if a<=b<=c or c<=b<=a:
  if abs(b-a)<=d and abs(c-b)<=d:
    print('Yes')
  else:
    print('No')
elif (b<a<=c or a<=c<b) or (b<c<=a or c<=a<b):
  if c-a<=d:
    print('Yes')
  else:
    print('No')