def solve(n, m):
    ret = 1
    for i in range(1, int(m ** 0.5) + 1):
        if m % i != 0:
            continue
        c = m // i
        if n * c <= m:
            return c
        elif n * i <= m:
            ret = i
    return ret


def main():
    n, m = map(int, input().split())
    print(solve(n, m))


if __name__ == "__main__":
    main()
    # for n in range(1, 500):
    #     for m in range(n, 1000):
    #         i = solve(n, m)
    #         assert m % i == 0, (n, m, i)
    #         assert n*i <= m, (n, m, i)
