A = int(input())

red = 0
blue = 0

p1 = input()

for i in range(0, A):
  x = p1[i]
  if x == 'B':
    blue += 1
  else:
    red += 1

if blue >= red:
  print('No')
else:
  print('Yes')
