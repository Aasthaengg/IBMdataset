r, g, b, n = map(int, input().split())

ans = 0

for i in range(n + 1):
    if i * r > n:
        break
    for j in range(n + 1):
        if i * r + j * g > n:
            break
        bnum = n - i * r - j * g
        if bnum % b == 0:
            ans += 1
print(ans)
