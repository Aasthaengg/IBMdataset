import collections
import sys

s=input()
S=collections.Counter(x for x in s)

a=S['a']
b=S['b']
c=S['c']

L=set([x for x in s])

if len(s)==1:
  print('YES')
  sys.exit()
elif len(s)==2:
  if len(L)==2:
    print('YES')
  else:
    print('NO')
  sys.exit()
elif len(s)==3:
  if len(L)==3:
    print('YES')
  else:
    print('NO')
  sys.exit()

if a==b and b==c:
  print('YES')
elif a==b:
  if min(b,c)+1==max(b,c):
    print('YES')
  else:
    print('NO')
else:
  if min(a,b)+1==max(a,b):
    if a==c or b==c:
      print('YES')
    else:
      print('NO')
  else:
    print('NO')