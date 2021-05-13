a,b,c=map(int,input().split())
f=False
for i in range(10**4):
  if (i*a)%b==c:
    f=True
    break
if f:
  print('YES')
else:
  print('NO')