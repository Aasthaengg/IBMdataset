import sys
input = sys.stdin.readline

from heapq import heappop, heappush
from collections import defaultdict

N, Q = map(int, input().split())

lst = []
l_append = lst.append
for i in range(N):
    s, t, x = map(int, input().split())
    l_append((t - x, 0, x)) #xで止まらなくなる
    l_append((s - x, 1, x)) #xで止まる

for i in range(Q):
    l_append((int(input()), 2, i))

lst.sort()
ans = [-1] * Q

#引っかかっている場所の管理
se = set()
se_hp = [] #heapで最小値を先頭に保つ

#小さい時刻から順に見ていく
# s_remove = se.remove
# s_add = se.add
for a, b, c in lst:
    if b == 0:
        se.remove(c)
    elif b == 1:
        se.add(c)
        heappush(se_hp, c)
    else:
        while se_hp and se_hp[0] not in se:
            heappop(se_hp)
        ans[c] = se_hp[0] if se_hp else -1

print ('\n'.join(map(str, ans)))