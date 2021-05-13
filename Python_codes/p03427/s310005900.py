import math
n = int(input())
k = int(math.log10(n))

a = n // (10 ** k)
b = n % (10 ** k)

if k == 0:
  ans = n
elif n % 10 == 9:
  ans = k * 9 + a
else:
  ans = k * 9 + a -1

print(ans)