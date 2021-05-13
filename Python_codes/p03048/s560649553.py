r, g, b, n = map(int, input().split())
cnt = 0

for i in range(n + 1):
    for j in range(n + 1):
        tmp = n - i * r  - j * g
        if 0 <= tmp and tmp % b == 0:
            cnt += 1
print(cnt)