n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

ans = 0
for i in range(n):
   x = 0
   row = 0
   for j in range(n):
      x += a[row][j]
      if i == j:
         row += 1
         x += a[row][j]
   ans = max(ans, x)

print(ans)
