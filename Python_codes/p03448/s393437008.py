a, b, c, x = (int(input()) for _ in range(4))
cnt = 0
for i in range(min(a, x // 500) + 1):
    for j in range(min(b, (x - 500 * i) // 100) + 1):
        if (x - 500 * i - 100 * j) // 50 <= c:
            cnt += 1
print(cnt)