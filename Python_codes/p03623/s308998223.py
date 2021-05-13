s=list(input().split())
x=int(s[0])
a=int(s[1])
b=int(s[2])
ave=(a+b)/2
if ave>x:
  if b>a:
    print('A')
  else:
    print('B')
else:
  if b>a:
    print('B')
  else:
    print('A')