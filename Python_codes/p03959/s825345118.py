#!/usr/bin/env python3

import collections
import functools


MOD = 10 ** 9 + 7
INF = MOD


def product_mod(seq, mod=MOD):
    return functools.reduce(lambda x, y: x * y % mod, seq, 1) % mod


Mountain = collections.namedtuple("Mountain", "ub lb")


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    ys = [int(y) for y in input().split()]
    ms = [Mountain(INF, 1) for _ in range(n)]
    ns = [Mountain(INF, 1) for _ in range(n)]
    ms[0] = Mountain(xs[0], xs[0])
    ns[-1] = Mountain(ys[-1], ys[-1])
    for idx in range(1, n):
        if xs[idx - 1] < xs[idx]:
            ms[idx] = Mountain(xs[idx], xs[idx])
        else:
            ms[idx] = Mountain(xs[idx], ms[idx].lb)
    for idx in range(n - 1)[::-1]:
        if ys[idx + 1] < ys[idx]:
            ns[idx] = Mountain(ys[idx], ys[idx])
        else:
            ns[idx] = Mountain(ys[idx], ns[idx].lb)
    hs = (Mountain(min(m.ub, n.ub), max(m.lb, n.lb)) for m, n in zip(ms, ns))
    ans = product_mod(max(h.ub - h.lb + 1, 0) for h in hs)
    print(ans)


if __name__ == '__main__':
    main()
