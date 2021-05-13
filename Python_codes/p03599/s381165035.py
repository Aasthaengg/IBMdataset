def main():
    A, B, C, D, E, F = list(map(int, input().split(' ')))
    ans_total, ans_sugar = 100 * A, 0
    a = 0
    while 100 * A * a <= F:
        b = 0
        while 100 * (A * a + B * b) <= F:
            if a == b == 0:
                b += 1
                continue
            c = 0
            while 100 * (A * a + B * b) + C * c <= F:
                if E * (A * a + B * b) < C * c:
                    break
                d = 0
                while 100 * (A * a + B * b) + C * c + D * d <= F:
                    if E * (A * a + B * b) < C * c + D * d:
                        break
                    sugar, total = C * c + D * d, 100 * (A * a + B * b) + C * c + D * d
                    if sugar * ans_total > ans_sugar * total:
                        ans_sugar = sugar
                        ans_total = total
                    d += 1
                c += 1
            b += 1
        a += 1
    print('{} {}'.format(ans_total, ans_sugar))


if __name__ == '__main__':
    main()
