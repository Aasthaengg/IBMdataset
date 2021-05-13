n = int(input())
ans = 10**n - 9**n - 9**n + 8**n
if n == 0 or n == 1:
  print(0)
  exit()
print(ans%(10**9+7))