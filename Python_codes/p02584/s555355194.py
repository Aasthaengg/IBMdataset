x, k, d = map(int, input().split())
x = abs(x)
if k * d < x:
    ans = x - k * d
else:
    if (k - x // d) % 2 == 0:
        ans = x % d
    else:
        ans = abs(x % d - d)
print(ans)
