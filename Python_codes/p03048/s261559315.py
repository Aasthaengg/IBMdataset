r, g, b, n = map(int, input().split())
cnt = 0

for i in range(n // r + 2):
    for j in range(n // g + 2):
        k = n - i * r - j * g
        if k < 0:continue
        if k % b == 0:cnt += 1
print(cnt)