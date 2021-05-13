# coding: utf-8

# https://atcoder.jp/contests/abc116


def main():
    s = int(input())
    a = [s]

    i = 1
    while True:
        ai = a[i-1] // 2 if a[i-1] % 2 == 0 else 3 * a[i-1] + 1
        if ai in a:
            return i+1
        a.append(ai)
        i += 1


print(main())
