def main():
    from math import ceil
    from itertools import accumulate
    from bisect import bisect_left
    n, h, *ab = map(int, open(0).read().split())

    x = max(ab[::2])
    *y, = filter(lambda i: i >= x, ab[1::2])
    y = sorted(y, reverse=True)
    *z, = accumulate(y)

    if z[-1] <= h:
        print(len(y) + ceil((h - z[-1]) / x))
    else:
        print(bisect_left(z, h) + 1)


if __name__ == '__main__':
    main()
