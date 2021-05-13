def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    for i in range(n):
        for j in range(n - 1):
            a[i][j] -= 1
    pt = [0] * n
    q = [[0, i] for i in range(n)]
    q = collections.deque(q)
    now = 0
    fq = collections.defaultdict(int)
    md = 0
    while True:
        if len(q) != 0:
            d, p = q.popleft()
            if d == now:
                o = a[p][pt[p]]
                r = a[o][pt[o]]
                if p == r and p not in fq and o not in fq:
                    fq[p]
                    fq[o]
                    md = max(md, d)
                    if len(a[p]) > pt[p] + 1:
                        pt[p] += 1
                        q.append([d + 1, p])
                    if len(a[o]) > pt[o] + 1:
                        pt[o] += 1
                        q.append([d + 1, o])
            else:
                q.append([d, p])
                fq = collections.defaultdict(int)
                now += 1
        else:
            break
    print(md + 1 if sum(pt) == (n - 2) * n else -1)


if __name__ == '__main__':
    slove()
