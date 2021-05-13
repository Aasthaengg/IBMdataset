d, n = map(int, input().split())
if n == 100:
  print(str(101) + ('00' * d))
else:
  print(str(n) + ('00' * d))