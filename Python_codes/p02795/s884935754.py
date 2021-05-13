h = int(input())
w = int(input())
n = int(input())
m = max(h, w)
if n % m:
  print(n // m + 1)
else:
  print(n // m)