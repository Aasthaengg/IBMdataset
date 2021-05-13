a,b,c,d=list(map(int,input().split()))
if abs(a-c)<=d:
  print('Yes')
  exit()
if abs(c-b)<=d and abs(b-a)<=d:
  print('Yes')
  exit()
print('No')