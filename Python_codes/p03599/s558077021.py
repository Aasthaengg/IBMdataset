def main():
    from itertools import combinations
    a, b, c, d, e, f = map(int, input().split())
    a *= 100
    b *= 100

    water = [a * i + b * j for i in range(f // a + 1) for j in range(f // b + 1)]
    sugar = [c * i + d * j for i in range(f // c + 1) for j in range(f // d + 1)]
    water.sort()
    sugar.sort(reverse=True)

    tmp = 0
    x, y = 0, 0
    for w in water:
        if w == 0:
            continue
        for s in sugar:
            if s + w > f:
                continue
            if s * 100 <= e * w and tmp <= s / (s + w):
                tmp = s / (s + w)
                x = s + w
                y = s
    print(x,y)


if __name__ == '__main__':
    main()
