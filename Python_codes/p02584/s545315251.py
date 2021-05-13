import sys
import math

X, K, D = [int(i) for i in input().split()]

x = (abs(X) - K * D)
if x >= 0:
  print(x)
  sys.exit()

a = X // D if X > 0 else math.ceil(X / D)
k = K - a
k = k % 2

print(abs(X - D * a - k * D if X > 0 else X - D * a + k * D))
