n = int(input())

ans = 0
for j in range(1, n+1):
    y = n // j
    ans += y * (2 * j + (y - 1) * j) // 2

print(ans)