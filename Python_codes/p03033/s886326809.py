import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())

STX = [list(map(int, input().split())) for _ in range(N)]
# xの昇順に工事の区間をsort
STX = sorted(STX, key=lambda x: x[2])

D = [int(input()) for _ in range(Q)]
ans = [-1] * Q
index = [-1] * Q
for s, t, x in STX:
    left = bisect.bisect_left(D, s - x - 0.5)
    right = bisect.bisect_left(D, t - x - 0.5)
    now = left
    while now < right:
        if index[now] == -1:  # まだansが更新されていない場合
            ans[now] = x
            index[now] = right
            now += 1
        else:
            now = index[now]
            

for a in ans:
    print(a)