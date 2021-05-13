'''input
5 5
.#.#.
#.#.#
.#.#.
#.#.#
.#.#.
'''

import sys
import math
from collections import Counter

debug = 0
readln = sys.stdin.readline
#sys.setrecursionlimit(1000000)

def write(s):
    sys.stdout.write(str(s))

def writeln(s):
    sys.stdout.write(str(s))
    sys.stdout.write('\n')

def readint():
    return int(readln().strip())

def readints():
    return map(int, readln().split())

def readstr():
    return readln().strip()

def readstrs():
    return readln().split()

def dbg(*args):
    if debug: print(' '.join(map(str, args)))


h,w = readints()
mat = []
dp = [[0] * w for _ in xrange(h)]
for _ in xrange(h):
    mat.append(readstr())

def getdp(r, c, cur):
    if r < 0 and c == 0 or c < 0 and r == 0:
        old = 0
        oldc = '.'
    elif r < 0 or c < 0:
        return 2**31
    else:
        old = dp[r][c]
        oldc = mat[r][c]

    if cur == '#' and oldc == '.':
        return old + 1
    else:
        return old

def solve(h, w):
    global dp
    for r in xrange(h):
        for c in xrange(w):
            cur = mat[r][c]
            dp[r][c] = min(getdp(r-1, c, cur), getdp(r, c-1, cur))
    dbg(dp)
    return dp[h-1][w-1]

print solve(h, w)