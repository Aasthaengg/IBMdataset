x=int(input())
s=str(input())
flag=0
if len(s)%2==0:
  n=len(s)//2
  for i in range(n):
    if s[i]!=s[n+i]:
      flag=1
else:
  flag=1
if flag==0:
  print('Yes')
else:
  print("No")