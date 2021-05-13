N = int(input())
flag = True
for i in range(N):
  n = int(input())
  if n % 2 == 1:
    flag = False
if flag:
  print('second')
else:
  print('first')