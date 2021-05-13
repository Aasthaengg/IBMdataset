from math import ceil
x = int(input())
ans = ceil(x*2/11)
if x % 11 == 6:
  ans -= 1
print(ans)