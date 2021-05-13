from bisect import bisect_right
from collections import defaultdict
import sys
read = sys.stdin.readline

s = read()[:-1]
t = read()[:-1]
# 即時終了
if set(t) - set(s):
    print(-1)
    exit()

# 前処理
# 0based indexにおいてi文字目以降に文字cが出てくるidxを取得する

# 前処理の前処理、0文字目から見たときにその文字が何文字目にあるかを記録しておく
mojiidx = defaultdict(lambda: [])
for i, ss in enumerate(s + s):
    mojiidx[ss].append(i)

# i文字目において、次に文字cが出てくるのは何文字あと？
skiptable = []
for i in range(0, len(s)):
    tmp = {}
    for c, ls in mojiidx.items():
        tmp[c] = ls[bisect_right(ls, i)] - i
    skiptable.append(tmp)

# print(skiptable)

# 本処理
# 最初にうまく飛べる点を探索
for i, ss in enumerate(s):
    if ss == t[0]:
        now = i
        break

for tt in t[1:]:
    idx = now % len(s)
    now += skiptable[idx][tt]
print(now + 1)