n=int(input())
s=input()
if n%2==1:
  print('No')
else:
  a=s[0:n//2]
  b=s[n//2:n]
  if a==b:
    print('Yes')
  else:
    print('No')