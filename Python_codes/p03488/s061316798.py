from itertools import groupby
from sys import stdin
from numpy import logical_or, zeros


def solve(s, p, q):

    ss = [list(g) for k, g in groupby(s)]
    len_sss = [len(sss) for sss in ss]
    ss_and_len = list(zip(ss, len_sss))
    is_start_with_TT = True if ss[0][0] == 'T' and 0 < len_sss[0] else False
    dir = 0
    dx, dy = [], []

    for sss, l in ss_and_len:
        if sss[0] == 'T':
            dir += l
        elif sss[0] == 'F':
            if dir % 2 == 0:
                dx.append(l)
            else:
                dy.append(l)

    len_dx = len(dx)
    len_dy = len(dy)

    _n = max(sum(dx), sum(dy))
    __n = _n*2+1
    if _n < abs(p) or _n < abs(q):
        return 0

    if 0 < len_dx:
        dpx = zeros((len_dx, __n), dtype='uint64')
        if is_start_with_TT:
            dpx[0][_n-dx[0]] = 1
        dpx[0][_n+dx[0]] = 1

        for i in range(1, len_dx):
            s = dx[i]
            dpx[i][:s] = dpx[i-1][s:2*s]
            dpx[i][s:-s] = logical_or(dpx[i-1][:-2*s], dpx[i-1][2*s:])
            dpx[i][-s:] = dpx[i-1][-2*s:-s]
    else:
        dpx = [[0]*__n]
        dpx[0][_n] = 1

    if 0 < len_dy:
        dpy = zeros((len_dy, __n), dtype='uint64')
        dpy[0][_n+dy[0]] = 1
        dpy[0][_n-dy[0]] = 1

        for i in range(1, len_dy):
            s = dy[i]
            dpy[i][:s] = dpy[i-1][s:2*s]
            dpy[i][s:-s] = logical_or(dpy[i-1][:-2*s], dpy[i-1][2*s:])
            dpy[i][-s:] = dpy[i-1][-2*s:-s]
    else:
        dpy = [[0]*__n]
        dpy[0][_n] = 1
    # print(dpx[-1])
    # print(dpy[-1])

    return dpx[-1][_n+p] and dpy[-1][_n+q]


if __name__ == '__main__':
    s = stdin.readline()
    p, q = map(int, input().split())

    print('Yes' if solve(s, p, q) else 'No')
