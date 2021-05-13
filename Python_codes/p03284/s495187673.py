n, k = map(int, input().split())
if k == 1:
  print(0)
  exit()
print(int(n % k != 0))