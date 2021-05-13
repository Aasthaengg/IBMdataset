a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>=b:
  if c>=d:
    print(b+d)
  else:
    print(b+c)
else:
  if c>=d:
    print(a+d)
  else:
    print(a+c)