k, a, b = map(int, input().split())
if k <= a or b - a <= 2:
    ans = 1 + k
elif b - a > 2:
    ans = ((k - a + 1) // 2) * (b - a) + a + (k - a + 1) % 2
print(ans)