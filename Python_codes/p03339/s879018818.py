def main():
    from itertools import accumulate
    n = int(input())
    f = lambda x: 1 if x == "W" else 0
    *s, = map(f, list(input()))
    t = list(accumulate(s))
    u = t[-1]
    ans = n

    for i, (j, k) in enumerate(zip(s, t)):
        m = (k - j) + (n - 1 - i) - (u - k)
        ans = min(ans, m)
    print(ans)


if __name__ == '__main__':
    main()
