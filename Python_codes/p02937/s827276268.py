
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
# 0文字目から見たときにその文字が何文字目にあるかを記録しておく
mojiidx = defaultdict(lambda: [])
for i, ss in enumerate(s + s):
    mojiidx[ss].append(i)

# 本処理
# 最初にうまく飛べる点を探索
for i, ss in enumerate(s):
    if ss == t[0]:
        now = i
        break

for tt in t[1:]:
    idx = now % len(s)
    # 前処理の列から文字ttが何文字あとに出現するかを探索する
    ls = mojiidx[tt]
    tmp = ls[bisect_right(ls, idx)] - idx
    now += tmp
print(now + 1)