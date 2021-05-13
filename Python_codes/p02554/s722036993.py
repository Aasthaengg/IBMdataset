def solve(n):
    a, b, c, m = 1, 1, 1, 1
    mod = 1000000007
    while n > 0:
        if n & 1:
            a = (a * 10 ** m) % mod
            b = (b * 9 ** m) % mod
            c = (c * 8 ** m) % mod
        n >>= 1
        m *= 2
    print((a - 2*b + c) % mod)

solve(int(input()))