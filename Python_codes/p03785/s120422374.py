import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import defaultdict
from math import floor
def main():
    n, c, k = map(int, input().split())
    times = defaultdict(int)
    for _ in range(n):
        times[int(input()) + k] += 1
    # ts:時間順に「時間ごとの出発したい人数」を並べたもの
    ts = dict(sorted(times.items()))

    r = 0
    busg = c # バスに乗せられる人数
    busstart = - k - 1
    for tse in ts:
        if busstart + k < tse: # 前のバスに間に合わない場合。バスを仕立てる
            r += floor(ts[tse] / c) # 満員になるバス台数を+する。
            nokori = ts[tse] % c
            if nokori: # 残りがいるならバスを仕立てる。
                r += 1
                busg = c - nokori
                busstart = tse
            else:
                busstart = -k - 1
        else:
            if busg >= ts[tse]: #バスに乗りきれる場合
                busg -= ts[tse]
            else:             # バスに乗り切れない場合。バスを仕立てる。
                r += floor(ts[tse] / c)
                nokori = ts[tse] % c
                if nokori:
                    r += 1
                    busg = c - nokori
                    busstart = tse
                else:
                    busstart = -k - 1
    print(r)

if __name__ == '__main__':
    main()