import sys
A,B,X = map(int,input().split())

if A > X:
  print('NO')
  sys.exit()
if A+B < X:
  print('NO')
  sys.exit()
  
print('YES')