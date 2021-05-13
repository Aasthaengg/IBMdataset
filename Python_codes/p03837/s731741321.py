import sys
import copy


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    wn, wm = list(map(int, readline().split()))
    inf = 10 ** 13
    wl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wl[i][i] = 0

    for i in range(wm):
        wa, wb, wc = list(map(int, input().rstrip('\n').split()))
        wl[wa - 1][wb - 1] = wc
        wl[wb - 1][wa - 1] = wc

    cwl = copy.deepcopy(wl)
    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wl[j][k] = min(wl[j][k], wl[j][i] + wl[i][k])
    cnt = 0
    for i in range(wn):
        for j in range(wn):
            if cwl[i][j] != 10 ** 13 and cwl[i][j] != wl[i][j]:
                cnt += 1
    print(cnt // 2)


if __name__ == '__main__':
    solve()
