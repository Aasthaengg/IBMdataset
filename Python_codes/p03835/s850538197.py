n, s = map(int, input().split())
ans = 0
for x in range(n+1):
  for y in range(n+1):
    if 0 <= s - x - y <= n:
        ans += 1
print(ans)