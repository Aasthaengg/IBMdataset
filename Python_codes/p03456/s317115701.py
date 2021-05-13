a, b = input().split()
num = int(a+b)

heihou = False

for i in range(1, 1000):
  if num == i*i:
    heihou = True
    break

if heihou:
  print('Yes')
else:
  print('No')