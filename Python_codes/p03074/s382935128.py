import sys
import collections
import bisect

input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

zerocnt = collections.Counter()
zeroindex = [-1] * N
onecnt = collections.Counter()
oneindex = [-1] * N

zh = oh = None
for i, x in enumerate(S):
    if x == "0":
        if i == 0 or S[i - 1] == "1":
            zh = i
    else:
        if i == 0 or S[i - 1] == "0":
            oh = i
    if zh is not None:
        zeroindex[i] = zh
        zerocnt[zh] += x == "0"
    if oh is not None:
        oneindex[i] = oh
        onecnt[oh] += x == "1"

zerolist = sorted(zerocnt.keys()) + [N]
onelist = sorted(onecnt.keys())


def solve():
    maxval = -1
    maxrange = None
    for i, head in enumerate(zerolist):
        zstart = max(i - K, 0)
        start = zerolist[zstart]
        if start > 0:
            assert S[start - 1] == "1"
            start = oneindex[start - 1]
        val = head - start
        if maxval < val:
            maxval = val
            maxrange = (start, head)
    return maxval


if len(zerocnt) <= K:
    print(N)
else:
    print(solve())
