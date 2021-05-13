n = int(input())
a = [list(map(int,input().split())) for _ in range(2)]

ans = 0
for i in range(n):
  candy = 0
  for j in range(n):
    if j <= i:
      candy += a[0][j]
    if j >= i:
      candy += a[1][j]
  ans = max(ans, candy)

print(ans)