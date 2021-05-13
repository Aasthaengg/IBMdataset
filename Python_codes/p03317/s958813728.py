def main():
    from math import ceil
    n, k, *a = map(int, open(0).read().split())
    ans = 1 + ceil((n - k) / (k - 1))
    print(ans)


if __name__ == '__main__':
    main()
