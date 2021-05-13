k, a, b = map(int, input().split())
if a+ 1 >= b:
    ans = k + 1
else:
    if k - a - 1 <  0:
        ans = k + 1
    else:
        n = (k - a - 1) // 2
        m = (k - a - 1) % 2
        ans = b + n * (b - a) + m


print(int(ans))