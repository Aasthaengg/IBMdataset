x = []
while True:
  i = str(input())
  if i == '0':
    break
  else:
    x.append(i)
n = 0
for i in x:
  n += 1
  print('Case '+str(n)+': '+i)