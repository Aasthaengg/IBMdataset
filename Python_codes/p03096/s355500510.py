#!/usr/bin/env python2
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
from __future__ import division, print_function

import itertools
import os
import sys
from atexit import register
from cStringIO import StringIO
from collections import Counter

range = xrange

filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip

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
fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)


def main():
    n = int(input())
    c = [int(input()) for _ in range(n)]

    _c, prev = [], 0
    for i in range(n):
        if c[i] != prev:
            _c.append(c[i])
        prev = c[i]
    c = _c
    n = len(c)

    prev_occur = [0] * (2 * 10**5 + 1)
    res, counts = [1.0] * (n + 1), Counter()
    for i in range(n):
        ind = prev_occur[c[i]]
        if ind != 0:
            res[i + 1] = fmod(res[i] + res[ind])
        else:
            res[i + 1] = res[i]

        counts[c[i]] += 1
        prev_occur[c[i]] = i + 1

    print(int(res[-1]) % MOD)


if __name__ == '__main__':
    main()
