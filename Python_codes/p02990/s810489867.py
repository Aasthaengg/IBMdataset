N, K = list(map(int, input().split()))
P = 10 ** 9 + 7


def combination(n, r):
    if r == 0:
        return 1
    x = 1
    y = 1
    for i in range(n - r + 1, n + 1):
        x = (x * i % P)
    for i in range(1, r + 1):
        y = (y * i % P)
    y_inv = _power(y, P - 2)
    return (x * y_inv) % P


def _power(x, n):
    ans = 1
    while n > 0:
        if bin(n & 1) == bin(1):
            ans = (ans * x) % P
        x = (x * x) % P
        n = n >> 1
    return ans


for i in range(1, K + 1):
    if i - 1 <= N - K:
        print((combination(K - 1, i - 1) * combination(N - K + 1, i)) % P)
    else:
        print(0)
