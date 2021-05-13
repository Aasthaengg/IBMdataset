import math
n = int(input())
ar = input()
w = 0
r = 0
ans = 0
for i in ar:
  if i == 'W':
    w += 1
  else:
    r += 1
if w == 0 or r == 0:
  print(ans)
else:
  for j in range(-1,-len(ar)-1,-1):
    if w == 0:
      break
    if ar[j] == 'R':
      ans += 1
    w -= 1
  print(ans)