def main():
    a, b, c, d, e, f = map(int, input().split())
    x, y = set(), set()
    for i in range(f // (100 * a) + 1):
        for j in range((f - 100 * a * i) // (100 * b) + 1):
            x.add(100 * a * i + 100 * b * j)
    for i in range(f // c + 1):
        for j in range((f - c * i) // d + 1):
            y.add(c * i + d * j)
    m = (-1, -1, -1)
    for xi in x:
        for yi in y:
            if xi == 0:
                continue
            if xi + yi > f:
                continue
            if 100 * yi > xi * e:
                continue
            s = yi / (xi + yi)
            if s > m[0]:
                m = (s, xi + yi, yi)
    print(m[1], m[2])


if __name__ == '__main__':
    main()