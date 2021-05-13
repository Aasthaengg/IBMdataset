def main():
    from collections import Counter
    n, *a = map(int, open(0).read().split())
    c = Counter(a)
    if n % 2 == 0:
        f = all(x == 2 for x in c.values())
    else:
        g = c.pop(0) == 1
        f = all(x == 2 for x in c.values()) and g
    ans = 2 ** (n // 2) % 1000000007 if f is True else 0
    print(ans)


if __name__ == '__main__':
    main()
