A = list(map(str,input().split()))
a = A.count('1')
b = A.count('7')
c = A.count('9')
d = A.count('4')
if a == b == c == d == 1:
  print('YES')
else:
  print('NO')