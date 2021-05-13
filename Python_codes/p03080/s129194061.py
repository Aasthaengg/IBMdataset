N = int(input())
S = input()
red = 0
blue = 0
for s in S:
  if s == 'R':
    red += 1
  if s == 'B':
    blue += 1
if red > blue:
  print('Yes')
else:
  print('No')
