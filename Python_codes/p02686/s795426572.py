import os

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N = int(sys.stdin.buffer.readline())
S = [sys.stdin.buffer.readline().decode().rstrip() for _ in range(N)]


def solve():
    diffs = []
    max_downs = []
    for s in S:
        diff = 0
        mi = 0
        for c in s:
            diff += 1 if c == '(' else -1
            mi = min(diff, mi)
        diffs.append(diff)
        max_downs.append(-mi)

    if sum(diffs) != 0:
        return False

    positives = []
    zeros = []
    negatives = []
    for i, d in enumerate(diffs):
        if d > 0:
            positives.append((max_downs[i], d, i))
        elif d < 0:
            negatives.append(((-max_downs[i] - d), d, i))
        else:
            zeros.append((max_downs[i], d, i))

    positives.sort()
    zeros.sort()
    negatives.sort()
    pos = 0
    for down, diff, i in positives:
        if down > pos:
            return False
        pos += diff
    for down, diff, i in zeros:
        if down > pos:
            return False
        pos += diff
    for down, diff, i in negatives:
        pos += diff
        down = -down
        if down > pos:
            return False

    assert pos == 0
    return True


ok = solve()
if ok:
    print('Yes')
else:
    print('No')
