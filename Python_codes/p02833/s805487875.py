import sys

n = int(input())
if n % 2 == 1:
  print(0)
  sys.exit()
ans = 0
x = 2
while n >= x:
  x *= 5
  ans += n // x
print(ans)