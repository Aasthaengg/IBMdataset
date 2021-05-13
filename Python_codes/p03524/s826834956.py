s=input()
a=s.count('a')
b=s.count('b')
c=s.count('c')
if len(set(list(s)))==1 and len(s)>1:
  print('NO')
elif len(set(list(s)))==2 and len(s)>2:
  print('NO')
elif abs(a-b)<=1 and abs(b-c)<=1 and abs(c-a)<=1:
  print('YES')
else:
  print('NO')