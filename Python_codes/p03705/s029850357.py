n, a, b = map(int, input().split())

if b - a > n + 1:
    ans = 0
elif a > b:
    ans = 0
else:
    diff = b - a
    ans = (b - a) * (n - 2) + 1
print(ans)