def main():
    from collections import Counter
    from itertools import accumulate
    s = input()

    n = 2019
    l = [0]
    t = 1
    for i, x in enumerate(s[::-1]):
        t = t * 10 % n
        y = (l[-1] + int(x) * t) % n
        l.append(y)

    c = Counter(l)
    ans = accumulate([v * (v - 1) // 2 for v in c.values()])
    print(list(ans)[-1])


if __name__ == '__main__':
    main()
