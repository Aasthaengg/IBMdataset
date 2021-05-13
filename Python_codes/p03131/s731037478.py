k, a, b = map(int, input().split())
ans = k + 1
if b > a:
    ans = max(ans, (k - a + 1) // 2 * (b - a - 2) + k + 1)
print(ans)