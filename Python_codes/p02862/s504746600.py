X, Y = list(map(int, input().split()))
P = 10 ** 9 + 7


def conb(n, r):
    x = 1
    y = 1
    for i in range(n - r + 1, n + 1):
        x = (x * i % P)
    for i in range(1, r + 1):
        y = (y * i % P)
    y_inv = power(y, P - 2)
    return (x * y_inv)%P


def power(x, n):
    ans = 1
    while (n > 0):
        if (bin(n & 1) == bin(1)):
            ans = (ans * x) % P
        x = (x * x) % P
        n = n >> 1  # ビットシフト
    return ans


if (2 * X - Y) % 3 == 0 and (2 * Y - X) % 3 == 0:
    u = (2 * Y - X) // 3
    r = (2 * X - Y) // 3
    if u < 0 or r < 0:
        print(0)
    else:
        print(conb(u + r, r))


else:
    print(0)
