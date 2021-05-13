s=list(str(input()))
n=len(s)
c=0
for i in range(n):
  if s[i]=='o':
    c+=1
t=15-n
if c+t>=8:
  print('YES')
else:
  print('NO')