import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
s_readline = sys.stdin.readline

N, K = map(int, readline().split())
S = list(map(int, s_readline().strip()))


def solve():
    s_grp = itertools.groupby(S)
    zl = []
    ol = []

    llen = 0
    f = False

    for k, l in s_grp:

        l = list(l)
        if k == 0:
            llen += len(l)
            f = True
        elif k == 1:
            ol.append(len(l))
            if f:
                llen += len(l)
                zl.append(llen)
                llen = 0

    else:
        if k == 0:
            zl.append(llen)

    if S[0] == 0:
        ol = [0] + ol

    # print(zl)
    # print(ol)

    zl_N = len(zl)

    zl_tsum = [0 for _ in range(zl_N + 1)]
    for i in range(zl_N):
        zl_tsum[i + 1] = zl_tsum[i] + zl[i]

    Km = min(K, zl_N)
    ans = 0
    for i in range(zl_N - Km + 1):
        t = zl_tsum[Km + i] - zl_tsum[i] + ol[i]
        ans = max(ans, t)

    print(ans)


if __name__ == '__main__':
    solve()
