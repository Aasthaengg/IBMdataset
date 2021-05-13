import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))

h, w, k = inpl()
s = [input()[:-1] for _ in range(h)]
ans = 10 ** 4
for t in itertools.product([0, 1], repeat=h-1):
    cnt = t.count(1)
    tmp = s[0]
    SW = []  # 縦方向に圧縮したマップを格納
    tmp = [int(s) for s in s[0]] # tmp[j]=横方向に切ったブロックのj列目の総和
    for i, c in enumerate(t):
        if c: #横に切る
            SW.append(tmp) # SWが確定する
            tmp = [int(s) for s in s[i + 1]] # 次弾装填
        else:
            tmp = [tmp[j] + int(s[i + 1][j]) for j in range(w)]
    SW.append(tmp)
    new_h = len(SW)  #圧縮後の高さ
    sums = [0] * new_h
    if max(itertools.chain.from_iterable(SW)) > k:
        # itertools.chain.from_iterable([[A,B],[C,D]]) -> A,B,C,D
        # 各マスの時点でダメだったらこの横の切り方ではだめ
        continue
    for j in range(w):
        sumtmp = [sums[i] + SW[i][j] for i in range(new_h)]
        if max(sumtmp) > k:
            # 左から足してみてどこかがkを超えるようなら切る
            cnt += 1
            sums = [SW[i][j] for i in range(new_h)]  #新しいSW[i][j]で上書き
        else:
            sums = sumtmp
    ans=min(ans,cnt)
print(ans)
