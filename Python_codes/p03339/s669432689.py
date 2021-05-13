def main():
    from itertools import accumulate
    n = int(input())
    s = input()
    s = s.replace("W", "1")
    s = s.replace("E", "0")
    s = [int(x) for x in s]

    t = list(accumulate(s))
    u = t[-1]
    ans = n

    for i, (j, k) in enumerate(zip(s, t)):
        m = (k - j) + (n - 1 - i) - (u - k)
        ans = min(ans, m)
    print(ans)


if __name__ == '__main__':
    main()
