import sys
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    a = [list(map(lambda x: int(x) - 1, input().rstrip('\n').split())) for _ in range(n)]
    ps = [0] * n
    ql = collections.deque()
    for i in range(n):
        ql.append([0, i])
    for i in range(10 ** 10):
        fq = collections.defaultdict(int)
        while ql:
            d, p = ql.popleft()
            if d == i:
                if ps[p] < n - 1:
                    np = a[p][ps[p]]
                    if ps[np] < n - 1:
                        rp = a[np][ps[np]]
                        if p == rp:
                            if p not in fq and np not in fq:
                                fq[p]
                                fq[np]
                                ps[p] += 1
                                if ps[p] < n - 1:
                                    ql.append([d+1, p])
                                ps[np] += 1
                                if ps[np] < n - 1:
                                    ql.append([d+1, np])
            else:
                ql.appendleft([d, p])
                break
        else:
            print(i + 1 if sum(ps) == n * (n - 1) else -1)
            exit()


if __name__ == '__main__':
    solve()
