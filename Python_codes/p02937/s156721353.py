from collections import defaultdict
from bisect import bisect_right

s = input()
ns = len(list(s))
t = input()
nt = len(list(t))

jisho = defaultdict(list)


# sの何文字目かどうかのidxを集める
for i in range(ns):
    jisho[s[i]].append(i)

# jishoにない→構成不可能
# 二分探索して今のidxより大きい値を取る。
# 今の値が一番大きいときは0からやり直す。
# 出力するのは先頭から何文字目か
now = -1  # bisect用の現在地
cnt = 0  # 何周したか
for i in range(nt):
    lis = jisho[t[i]]
    if not lis:
        print(-1)
        exit()
    pos = bisect_right(lis, now)
    # print(t[i], now, pos)
    # ここで復習、bisect_right はnow以下のものの個数。
    if pos == len(lis):
        now = -1
        cnt += 1
        pos = bisect_right(lis, now)
    now = lis[pos]
print(cnt * ns + now + 1)

