a, b, x = map(int, input().split())
if a % x == 0:
  alpha = a // x
else:
  alpha = a // x + 1
beta = b // x
print(beta - alpha + 1)