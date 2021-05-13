k, a, b = map(int, input().split())

ans = a + (b - a) * ((k - a + 1) // 2)
if (k - a) % 2 == 0:
    ans += 1
print(max(k + 1, ans))