n = int(input())
zeros = 0
ab = {}
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    if a == b == 0:
        zeros += 1
    elif a == 0 or b == 0:
        if None not in ab:
            ab[None] = [0, 0]
        if a == 0:
            ab[None][0] += 1
        else:
            ab[None][1] += 1
    else:
        x = 1 if a * b > 0 else -1
        c = max(abs(a) * 10 ** 100 // abs(b) * x,
                abs(b) * 10 ** 100 // abs(a) * (-x))
        if c not in ab:
            ab[c] = [0, 0]
        if a * b > 0:
            ab[c][0] += 1
        else:
            ab[c][1] += 1
ans = 1
mod = 10 ** 9 + 7
for _, v in ab.items():
    ans *= pow(2, v[0], mod) + pow(2, v[1], mod) - 1
    ans %= mod
ans += zeros - 1
print(ans % mod)
