n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = sorted(list(map(int, input().split())))
tx = 0
ty = 0
sx = 0
sy = 0
for i in range(n):
  tx += i * x[i] - sx
  sx += x[i]
for i in range(m):
  ty += i * y[i] - sy
  sy += y[i]
print(tx * ty % 1000000007)
