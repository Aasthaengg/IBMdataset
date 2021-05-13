def main():
    n, a, b, *x = map(int, open(0).read().split())
    ans = 0
    it = iter(x)
    nw = it.__next__()
    for nx in it:
        ans += min(b, (nx - nw) * a)
        nw = nx

    print(ans)


if __name__ == '__main__':
    main()
