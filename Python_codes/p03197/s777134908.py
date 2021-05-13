n = int(input())
flag = False
for i in range(n):
  k = int(input())
  if k%2 == 1:
    flag = True
    break
if flag:
  print('first')
else:
  print('second')