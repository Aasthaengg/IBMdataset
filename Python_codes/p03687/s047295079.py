import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import accumulate


def read():
    s = input().strip()
    return s,


def solve(s):
    z = defaultdict(list)
    for i in range(len(s)):
        z[s[i]].append(i)
    ans = 99999
    for k, v in z.items():
        prev = -1
        diffmax = 0
        for i in v:
            diffmax = max(diffmax, i-prev-1)
            prev = i
        diffmax = max(diffmax, len(s)-v[-1]-1)
        ans = min(ans, diffmax)
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
