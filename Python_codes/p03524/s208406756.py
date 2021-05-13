s=input()
x=s.count('a')
y=s.count('b')
z=s.count('c')
a=[x,y,z]
if len(s)==1:
  print('YES')
elif len(s)==2:
  if s[0]==s[1]:
    print('NO')
  else:
    print('YES')
else:
  if len(s)%3==0:
    if x==y and y==z:
      print('YES')
    else:
      print('NO')
  else:
    if max(a)-min(a)==1:
      print('YES')
    else:
      print('NO')