def main():
    a, b, c, d, e, f = map(int, input().split())
    a *= 100
    b *= 100
    m = (-1, 0, 0)
    for i in range(f // a + 1):
        for j in range((f - (a * i)) // b + 1):
            ma = a * i + b * j
            if ma == 0:
                continue
            for k in range((f - ma) // c + 1):
                if 100 * c * k > ma * e:
                    break
                for l in range((f - (ma + c * k)) // d + 1):
                    mb = c * k + d * l
                    if 100 * mb > ma * e:
                        break
                    dab = mb / (ma + mb)
                    if dab > m[0]:
                        m = (dab, ma + mb, mb)
    print(m[1], m[2])


if __name__ == '__main__':
    main()
