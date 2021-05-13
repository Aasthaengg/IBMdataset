n, a, b = map(int, input().split())
if abs(a - b) % 2 == 0:
    ans = abs(a - b) // 2
else:
    if abs(a - 1) > abs(n - b):
        a, b = n + 1 - b, n + 1 - a
    b -= a
    ans = abs(b - 1) // 2 + a
print(ans)