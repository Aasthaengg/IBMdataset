#!/usr/bin/env python3
import sys
import bisect

"""
ABC113_C ID 学び：
 python の0埋め　s.rjust(digit,0) でいける
 sortを県ごとにしないといけない、とわかれば、input, sort , outputの３段かいに別れる
どんな配列を持てばいいかは事前に考える。
実際にそこまで立てて、inputをローカルでやると良い
"""

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n, m = map(int, input().split())
lis_p = [[] for _ in range(n)]  # 県pに属する市の誕生年が入る
city = [[0, 0] for _ in range(m)]  # p と　idx
idx_p = []  # 何番目にそのcity が県pに追加されたかを記憶
# input
for i in range(m):
    p, y = map(int, input().split())
    city[i][0] = p - 1
    city[i][1] = y
    lis_p[p - 1].append(y)
for pref in range(n):
    k = len(lis_p[pref])
    # print(lis_p[pref])
    idx = []
    if k > 0:
        lis_p[pref], idx = zip(*sorted(zip(lis_p[pref], range(k))))
    idx_p.append(list(idx))
# print(lis_p, idx_p)
for i in range(m):
    # string になおす必要がある rjust
    print(str(city[i][0] + 1).rjust(6, "0"), end="")
    print(str(1 + bisect.bisect_left(lis_p[city[i][0]], city[i][1])).rjust(6, "0"))
