import sys
n = int(input())
if n == 0:
  print(0)
  sys.exit()
s = ''
while n != 0:
  s += str(n % 2)
  n -= n % 2
  n //= -2
print(s[::-1])
