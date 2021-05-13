import math
n, m = input().split()
n = int(n)
m = int(m)
x = 0
y = 0
if n > 1:
  x = int(math.factorial(n)/(2 * math.factorial(n-2)))
if m > 1:
  y = int(math.factorial(m)/(2 * math.factorial(m-2)))

print(x+y)

