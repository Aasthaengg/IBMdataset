#153_F
from bisect import bisect_right
n, d, a = map(int, input().split())
mons = sorted([tuple(map(int, input().split())) for _ in range(n)])
x = [mons[i][0] for i in range(n)]
h = [mons[i][1] for i in range(n)]
damage = [0 for _ in range(n+1)]
cnt = 0
for i in range(n):
    if i > 0:
        damage[i] += damage[i-1]
        if h[i] <= damage[i]:
            continue
    
    cur_cnt = -(-(h[i]-damage[i]) // a)
    cnt += cur_cnt
    damage[i] += cur_cnt * a
    idx = bisect_right(x, x[i] + 2 * d)
    damage[idx] -= cur_cnt * a
    
print(cnt)