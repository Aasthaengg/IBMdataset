x = []
for i in range(5):
  tmp = int(input())
  x.append(tmp)
k = int(input())

flag = 1
for i in range(len(x)-1):
  for j in range(len(x)):
    if x[j]-x[i] > k:
      flag = 0
      break
  if flag == 0:
    break
if flag == 0:
  print(':(')
else:
  print('Yay!')