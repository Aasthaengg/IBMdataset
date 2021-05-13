a, b = map(int, input().split())

if a == b:
    ans = a + b
else:
    m = max(a, b)
    ans = m + m - 1

print(ans)
