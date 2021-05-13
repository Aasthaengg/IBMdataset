def main():
    from itertools import tee, zip_longest

    N, T = map(int, input().split())
    *t, = map(int, input().split())

    iter_t = iter(t)
    next(iter_t)

    ans = sum(min(T, t1 - t0) for t0, t1 in zip_longest(t, iter_t, fillvalue=1 << 31))

    print(ans)


if __name__ == '__main__':
    main()
