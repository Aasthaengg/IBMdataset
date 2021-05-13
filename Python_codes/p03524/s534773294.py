s=input()
n=len(s)
set=set(s)
m=len(set)
a=s.count('a')
b=s.count('b')
c=s.count('c')
if m==1:
  if n==1:
    print('YES')
  else:
    print('NO')
elif m==2:
  if n==2:
    print('YES')
  else:
    print('NO')
else:
  if n%3==0:
    if a==b==c:
      print('YES')
    else:
      print('NO')
  elif n%3==2:
    if (a==n//3+1 and b==n//3+1) or (c==n//3+1 and b==n//3+1) or (a==n//3+1 and c==n//3+1):
      print('YES')
    else:
      print('NO')
  else:
    if (a==n//3 and b==n//3) or (c==n//3 and b==n//3) or (a==n//3 and c==n//3):
      print('YES')
    else:
      print('NO') 