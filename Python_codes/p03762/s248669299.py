n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
w = 0
ans = 0
for i in range(n - 1):
    w += (x[i + 1] - x[i]) * (i + 1) * (n - i - 1)
    w %= (10 ** 9 + 7)
for i in range(m - 1):
    ans += w * (y[i + 1] - y[i]) * (i + 1) * (m - i - 1)
    ans %= (10 ** 9 + 7)
print(ans)
