a, b, c = map(int, input().split())

x = 10 * a + b + c
y = a + 10 * b + c
z = a + b + 10 * c

ans = max(x, y, z)

print(ans)