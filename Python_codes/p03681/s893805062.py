import math
n, m = map(int, input().split())
diff = abs(n - m)

# 階乗は、factorial

if (diff > 1):
    print(0)
else:
    x = math.factorial(n)
    y = math.factorial(m)

    if (n == m):
        tt = 2
    else:
        tt = 1

    ans = tt * (x * y) % (10 ** 9 + 7)

    print(ans)
