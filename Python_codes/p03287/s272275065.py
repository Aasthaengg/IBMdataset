import sys
import itertools
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a = [v % m for v in list(itertools.accumulate(a))]
    cnt = a.count(0)
    d = collections.defaultdict(int)
    for v in a:
        cnt += d[v]
        d[v] += 1
    print(cnt)


if __name__ == '__main__':
    solve()
