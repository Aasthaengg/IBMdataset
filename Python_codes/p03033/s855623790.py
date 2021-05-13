import sys
s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2sss = lambda n: [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

# random_denseがTLE, 他はAC
"""
from bisect import bisect_left, bisect_right  # 二分探索
def main():
    N, Q = i2nn()
    STX = ii2nnn(N) # 座標 X で時刻 [S, T) が工事
    D = ii2nn(Q)    # 昇順ソート済み
    E = [-1] * Q
    STX.sort(key=lambda v: v[2])
    for s, t, x in STX:
        a = bisect_left(D, s-x)
        b = bisect_left(D, t-x)
        for i in range(a, b):
            if E[i] == -1:
                E[i] = x
    for e in E:
        print(e)
"""

def main():
    N, Q = i2nn()
    STX = ii2nnn(N) # 座標 X で時刻 [S, T) が工事
    D = ii2nn(Q)    # 昇順ソート済み

    events = []
    for s, t, x in STX:
        events.append(('S', s-x-0.25, x))
        events.append(('T', t-x-0.75, x))  # 0.5 同士だと [1, 2), [0, 1) で吹き飛ぶ
    for i, d in enumerate(D):
        events.append(('D', d, i))
    
    ans = [-1] * Q
    events.sort(key=lambda v: v[1])
    xset = set()
    xmin = 1e+10
    for event, time, xi in events:
        if event == 'S':
            xset.add(xi)
            if xmin > xi:
                xmin = xi
        elif event == 'T':
            xset.remove(xi)
            if xmin == xi:
                if xset:
                    xmin = min(xset)
                else:
                    xmin = 1e+10
        elif event == 'D' and xset:
            ans[xi] = xmin

    for n in ans:
        print(n)

main()
