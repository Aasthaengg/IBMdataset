n,k=map(int,input().split())
c=1
i=1
while i+2<=n:
    i+=2
    c+=1
if c>=k:
  print('YES')
else:
  print('NO')