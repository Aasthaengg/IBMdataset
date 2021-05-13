n, m = map(int, input().split())
cnt = 0
if n == 1 and m == 1:
  corner = 0
  wall = 0
if n > 1 and m > 1:
  corner = 4
  wall = max(0, n-2) * 2 + max(0, m-2) * 2
if n == 1 and m > 1:
  corner = 2
  wall = 0
if n > 1 and m == 1:
  corner = 2
  wall = 0
print(n * m - corner - wall)