# 丁度n本の辺を持つ完全グラフが存在するか？という問題
from itertools import combinations
from collections import defaultdict
n = int(input())
# edgeを入れるとnode数が取れる
dd = defaultdict(int)
prev = 0
for i in range(1, 10**5):
    if n < prev:
        break
    dd[prev] = i
    prev += i

if dd[n]:
    print('Yes')
    print(dd[n])
    # dd[n]頂点、n辺の完全グラフを構築する
    subarrays = [set()for _ in range(dd[n])]
    cnt = 1
    for i, j in combinations(range(dd[n]), 2):
        subarrays[i].add(cnt)
        subarrays[j].add(cnt)
        cnt += 1
    for s in subarrays:
        print(len(s), *s)

else:
    print('No')