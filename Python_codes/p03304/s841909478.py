#!/usr/bin/env python3


def main():
    n, m, d = (int(x) for x in input().split())
    a_at_d0 = (m - 1) / n
    if d == 0:
        res = a_at_d0
    else:
        unit = a_at_d0 * 2
        res = (n - d) / n * unit
    print("{:.10f}".format(res))


if __name__ == '__main__':
    main()
