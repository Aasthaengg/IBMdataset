r, g, b, n = map(int, input().split())

ans = 0

for x in range(n // r + 1):
    for y in range((n - r * x) // g + 1):
        z = (n - r * x - g * y) / b
        if z.is_integer():
            ans += 1

print(ans)