n, a, b = map(int, input().split())
x = list(map(int, input().split()))
now = x[0]
ans = 0
for i in range(1, n):
    ans += min(a*(x[i] - now), b)
    now = x[i]
print(ans)