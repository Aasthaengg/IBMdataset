from bisect import bisect_left
from itertools import accumulate

N,M = map(int,input().split())
A = sorted([int(i) for i in input().split()])

# 判定
def is_under_M(x:int):
    cnt = 0
    for i in range(N):
        # 幸福度x以上の個数を求める
        pos = bisect_left(A, x - A[i])
        cnt += N - pos
    return cnt < M

# 二分探索
ng, ok = 0, 2*(10**5)+1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_under_M(mid):
        ok = mid
    else:
        ng = mid
# ng, ok = X-1, X

# Aの累積和
Aacum = tuple(accumulate([0] + A))

ans = 0
for i in range(N):
    # 幸福度ok以上の個数を求める
    pos = bisect_left(A, ok - A[i])
    cnt = N - pos

    ans += cnt * A[i] + (Aacum[N] - Aacum[pos])
    M -= cnt

ans += M * ng

print(ans)