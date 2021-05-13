A,B,C = map(int, input().split())
k = 1
flag = False

while A*B >= A*k:
  if A*k % B == C:
    flag = True
  k += 1

if flag:
  print('YES')
else:
  print('NO')