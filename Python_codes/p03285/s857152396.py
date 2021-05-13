import math
n = int(input())
ans = ''
for i in range(math.floor(n / 4) + 1):
  if ans == '':
    m = n
    m -= 4 * i
    if m % 7 == 0:
      ans = 'Yes'
    else:
      next
if ans == '':
  ans = 'No'
print(ans)