n = int(input())
ans = 0
for i in range(1, n+1):
  cnt = 0
  x = i
  while x % 2 == 0:
    x //= 2
    cnt += 1
  ans = max(ans, cnt)
print(2 ** ans)