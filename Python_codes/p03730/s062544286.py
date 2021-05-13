a,b,c=map(int,input().split())
ch=0
for x in range(b):
  if (x*a)%b==c:
    ch+=1
    
if ch>0:
  print('YES')
else:
  print('NO')
