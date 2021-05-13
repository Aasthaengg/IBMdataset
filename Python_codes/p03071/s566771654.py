a, b = map(int, input().split())


if abs(a - b) > 0:
    m = max(a, b)
    ans = m + m - 1
else:
    ans = a + b

print(ans)
