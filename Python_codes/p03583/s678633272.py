def solve():
    N = int(input())
    M = 3501

    for h in range(1, M):
        for n in range(h, M):
            numerator = N * h * n
            denominator = 4 * n * h - N * h - N * n
            if numerator <= 0 or denominator <= 0:
                continue
            if numerator % denominator == 0:
                return h, n, numerator // denominator


h, n, w = solve()
print(h, n, w)
