import sys
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = [list(map(int, readline().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n - 1):
            a[i][j] -= 1
    ls = [0] * n
    ql = collections.deque()
    for i in range(n):
        ql.append([0, i])

    for i in range(10 ** 10):
        fq = collections.defaultdict(list)
        while True:
            if len(ql) != 0:
                d, ps = ql.popleft()
                if d == i:
                    if ps not in fq:
                        nw = a[ps][ls[ps]]
                        if nw not in fq:
                            rw = a[nw][ls[nw]]
                            if ps == rw:
                                fq[ps]
                                fq[nw]
                                ls[ps] += 1
                                ls[nw] += 1
                                if ls[ps] < n - 1:
                                    ql.append([d+1, ps])
                                if ls[nw] < n - 1:
                                    ql.append([d+1, nw])
                else:
                    ql.appendleft([d, ps])
                    break
            else:
                if sum(ls) == n * (n - 1):
                    print(i + 1)
                else:
                    print(-1)
                exit()


if __name__ == '__main__':
    solve()
