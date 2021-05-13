def main():
    N = int(input())
    A = (map(int, input().split()) for _ in range(2))

    def accumulate(a):
        s = 0
        yield s
        for x in a:
            s += x
            yield s

    Accs = tuple(
        tuple(accumulate(a)) for a in A
    )

    ans = 0
    for from_r0 in range(N):
        ans = max(ans, Accs[0][from_r0 + 1] + Accs[1][N] - Accs[1][from_r0])
    print(ans)


if __name__ == '__main__':
    main()
