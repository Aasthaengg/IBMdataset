def fact(a, mod):
    ret = 1
    for i in range(a):
        ret *= (i + 1)
        ret %= mod
    return ret


def main():
    MOD = 10**9 + 7
    N, M = list(map(int, input().split(' ')))
    if abs(N - M) > 1:
        print(0)
    elif abs(N - M) == 0:
        print((2 * fact(N, MOD) * fact(M, MOD)) % MOD)
    else:
        print((fact(N, MOD) * fact(M, MOD)) % MOD)


if __name__ == '__main__':
    main()