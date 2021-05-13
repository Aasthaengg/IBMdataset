k, a, b = map(int, input().split())

if 1 + k <= a or b - a <= 2:
    print(1 + k)
else:
    cnt = (k - (a - 1)) // 2
    mod = (k - (a - 1)) % 2
    ans = (b - a)*cnt + a + mod
    print(max(ans, k + 1))