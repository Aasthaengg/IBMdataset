#!/usr/bin/env python2
from __future__ import division, print_function

import itertools
import os
import sys
from atexit import register
from cStringIO import StringIO

range = xrange

sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = StringIO(os.read(0, os.fstat(0).st_size)).readline

MOD = 10**9 + 7
MODF = float(MOD)

MAGIC = 6755399441055744.0
SHRT = 65536.0

MODF_INV = 1.0 / MODF
SHRT_INV = 1.0 / SHRT

fround = lambda x: (x + MAGIC) - MAGIC
fmod = lambda a: a - MODF * fround(MODF_INV * a)


def main():
    n = int(input())
    c = [int(input()) for _ in range(n)]

    c = [x[0] for x in itertools.groupby(c)]
    n = len(c)

    res, prev = [1.0] * (n + 1), [0] * (2 * 10**5 + 1)
    for i in range(n):
        res[i + 1] = res[i] if prev[c[i]] == 0 else fmod(res[i] + res[prev[c[i]]])
        prev[c[i]] = i + 1

    print(int(res[-1]) % MOD)


if __name__ == '__main__':
    main()
