n=int(input())
s=input()
u=len(s)
if n%2==1:
  print('No')
else:
  if s[0:n//2]==s[n//2:n]:
    print('Yes')
  else:
    print('No')