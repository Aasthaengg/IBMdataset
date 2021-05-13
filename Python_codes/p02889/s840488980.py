import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m, l = list(map(int, input().rstrip('\n').split()))
    wn = n
    wm = m
    inf = 10 ** 11
    wl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wl[i][i] = 0

    for i in range(wm):
        wa, wb, wc = list(map(int, input().rstrip('\n').split()))
        wl[wa - 1][wb - 1] = wc
        wl[wb - 1][wa - 1] = wc

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wl[j][k] = min(wl[j][k], wl[j][i] + wl[i][k])

    wn = n
    wm = m
    inf = 10 ** 11
    wl2 = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wl2[i][i] = 0

    for i in range(wn):
        for j in range(wn):
            if wl[i][j] <= l:
                wl2[i][j] = 1

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wl2[j][k] = min(wl2[j][k], wl2[j][i] + wl2[i][k])

    q = int(input().rstrip('\n'))
    for i in range(q):
        s, t = list(map(int, input().rstrip('\n').split()))
        print(wl2[s-1][t-1] - 1 if wl2[s-1][t-1] != inf else -1)


if __name__ == '__main__':
    solve()
