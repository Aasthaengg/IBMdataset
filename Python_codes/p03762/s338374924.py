def main():
    MOD = 10 ** 9 + 7

    N, M = map(int, input().split())
    *X, = map(int, input().split())
    *Y, = map(int, input().split())

    def total(E):
        L = len(E)
        ret = 0
        for i, (frm, to) in enumerate(zip(E, E[1:]), start=1):
            ret = (ret + i * (L - i) * (to - frm)) % MOD
        return ret

    ans = total(X) * total(Y) % MOD
    print(ans)


if __name__ == '__main__':
    main()
