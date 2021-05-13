# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D
# Shell Sort
# Result:
import sys
import math

def insertion_sort(ary, g):
    cnt = 0
    ary_len = len(ary)
    for i in range(g, ary_len):
        v = ary[i]
        j = i - g
        while (j >= 0 and ary[j] > v):
            ary[j + g] = ary[j]
            j -= g
            cnt += 1
        ary[j + g] = v
    return cnt

def shell_sort(ary):
    ary_len = len(ary)
    gs = []
    v = ary_len
    while v > 0:
        gs.append(v)
        v >>= 1
    m = len(gs)

    cnt = 0
    for i in range(0, m):
        cnt += insertion_sort(ary, gs[i])
    return [m, gs, cnt]

lines = sys.stdin.readlines()
ary_len = int(lines.pop(0))
ary = map(int, lines)
assert ary_len == len(ary)

m, gs, cnt = shell_sort(ary)
print m
print ' '.join(map(str, gs))
print cnt
for v in ary:
    print v