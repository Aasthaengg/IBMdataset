N, K = map(int, input().split())

x, y = 0, 0

for i in range(1, N + 1):
    if i % K == 0:
        x += 1
    if K % 2 == 0 and i % K == K // 2:
        y += 1

print(x ** 3 + y ** 3)
