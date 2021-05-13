n, h, w = [int(item) for item in input().split()]
ans = 0
for i in range(n):
  x, y = [int(item) for item in input().split()]
  if x >= h and y >= w:
    ans += 1
print(ans)