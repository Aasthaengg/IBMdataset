a,b,x=map(int,input().split())
if a>x:
  print('NO')
  exit()
if x-a<=b:
  print('YES')
  exit()
print('NO')