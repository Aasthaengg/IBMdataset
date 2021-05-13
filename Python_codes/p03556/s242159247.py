import math
n = int(input())
ans = 0
for i in range(int(math.sqrt(n)) + 1):
  if i ** 2 > n:
    exit()
  elif i ** 2 > ans and i ** 2 <= n:
    ans = i ** 2
print(ans)