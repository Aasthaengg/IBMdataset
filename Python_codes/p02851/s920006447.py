import sys
import itertools
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    a = list(map(lambda x: int(x) - 1, readline().split()))
    a = [0] + [i % k for i in list(itertools.accumulate(a))]
    d = collections.defaultdict(int)
    cnt = 0
    for i in range(n + 1):
        cnt += d[a[i]]
        d[a[i]] += 1
        if i >= k - 1:
            d[a[i-k+1]] -= 1
    print(cnt)


if __name__ == '__main__':
    solve()
