import collections


def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    for i in range(n):
        for j in range(n-1):
            a[i][j] -= 1
    ad = [0] * n
    q = collections.deque([[0, i] for i in range(n)])
    for i in range(10 ** 20):
        fq = collections.defaultdict(list)
        while True:
            if len(q) != 0:
                d, p = q.popleft()
                if d == i:
                    if p not in fq:
                        tp = a[p][ad[p]]
                        if tp not in fq:
                            if p == a[tp][ad[tp]]:
                                fq[tp]
                                fq[p]
                                ad[tp] += 1
                                ad[p] += 1
                                if ad[tp] < n - 1:
                                    q.append([d+1, tp])
                                if ad[p] < n - 1:
                                    q.append([d+1, p])
                else:
                    q.appendleft([d, p])
                    break
            else:
                if sum(ad) == n * (n - 1):
                    print(i + 1)
                else:
                    print(-1)
                exit()


if __name__ == '__main__':
    slove()
