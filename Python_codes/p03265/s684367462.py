# coding: utf-8

# https://atcoder.jp/contests/abc108


def main():
    x1, y1, x2, y2 = map(int, input().split())

    v12 = (x2-x1, y2-y1)
    v23 = (-v12[1], v12[0])
    v34 = (-v23[1], v23[0])
    v41 = (-v34[1], v34[0])

    x3, y3 = x2+v23[0], y2+v23[1]
    x4, y4 = x3+v34[0], y3+v34[1]

    print("{} {} {} {}".format(x3, y3, x4, y4))


main()
# print(main())
