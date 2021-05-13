n=int(input())
s=input()
b=0
r=0
for i in range(0,n):
  if s[i]=='B':
    b=b+1
  else:
    r=r+1
if r>b:
  print('Yes')
else:
  print('No')