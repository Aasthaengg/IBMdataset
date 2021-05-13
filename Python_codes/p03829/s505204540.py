n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    xs = x[i + 1] - x[i]
    if xs * a < b:
        ans += xs * a
    else:
        ans += b

print(ans)
