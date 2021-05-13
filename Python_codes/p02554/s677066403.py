n = int(input())
if n == 1:
  print(0)
  exit()

print((10**n-9**n+8**n-9**n)%(10**9+7))
