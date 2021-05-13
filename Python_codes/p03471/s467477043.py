N, Y = map(int, input().split())
x = y = z = -1

for i in reversed(range(N + 1)): # 10000
  for j in reversed(range(N + 1)): # 5000
    n = Y - 10000 * i - 5000 * j
    if n >= 0 and n % 1000 == 0:
      k = n // 1000
      if i + j + k == N:
        x, y, z = i, j, k
        break

print(x, y, z)