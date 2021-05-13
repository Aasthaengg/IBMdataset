n = int(input())
s = input()
red = 0
for i in range(n):
  if s[i] == 'R':
    red += 1
if red * 2 > n:
  print('Yes')
else:
  print('No')