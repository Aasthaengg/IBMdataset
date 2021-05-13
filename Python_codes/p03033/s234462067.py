# https://atcoder.jp/contests/abc128/submissions/8312583
# 写経

def solve():
    from heapq import heappush, heappop
    from collections import defaultdict
    from operator import itemgetter
    import sys

    input = sys.stdin.readline

    inf = 1 << 31

    n, q = map(int, input().split())

    S = [0] * n
    T = [0] * n
    X = [0] * n
    for i in range(n):
        S[i], T[i], X[i] = map(int, input().split())

    e = [(t - x, 0, x) for t, x in zip(T, X)]
    e.extend([(s - x, 1, x) for s, x in zip(S, X)])
    e.extend([(int(input()), 2, idx) for idx in range(q)])
    # e = [*((t - x, 0, x) for t, x in zip(T, X)),
    #      *((s - x, 1, x) for s, x in zip(S, X)),
    #      *((int(input()), 2, idx) for idx in range(q))
    #      ]
    e.sort(key=itemgetter(0))
    # 安定ソートなので、0,1,2順になる（はず

    cnt = defaultdict(int)
    cnt[inf] = 1
    h = [inf]
    ret = [-1] * q
    for time, type, x in e:
        if type == 0:
            cnt[x] -= 1
        elif type == 1:
            heappush(h, x)
            cnt[x] += 1
        else:
            while not (cnt[h[0]]):
                heappop(h)
            curr = h[0]
            if curr != inf:
                ret[x] = curr

    print(*ret, sep='\n')


if __name__ == '__main__':
    solve()
