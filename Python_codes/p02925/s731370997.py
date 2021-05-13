import sys
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = [list(map(lambda x: int(x) - 1, readline().split())) for _ in range(n)]
    ls = [0] * n
    ql = [[0, i] for i in range(n)]
    ql = collections.deque(ql)
    for i in range(10 ** 10):
        fq = collections.defaultdict(int)
        while ql:
            d, p = ql.popleft()
            if d == i:
                if ls[p] < n - 1:
                    rp = a[p][ls[p]]
                    if ls[rp] < n - 1:
                        rrp = a[rp][ls[rp]]
                        if p == rrp:
                            if p not in fq and rp not in fq:
                                fq[p]
                                fq[rp]
                                if ls[p] + 1 < n:
                                    ls[p] += 1
                                    ql.append([d+1, p])
                                if ls[rp] + 1 < n:
                                    ls[rp] += 1
                                    ql.append([d+1, rp])
            elif d > i:
                ql.appendleft([d, p])
                break
        if len(ql) == 0:
            print(i if sum(ls) == (n - 1) * n else -1)
            exit()


if __name__ == '__main__':
    solve()
