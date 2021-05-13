# https://atcoder.jp/contests/abc103/tasks/abc103_d

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
schedule = []
for i in range(M):
    start, end = map(int, input().split())
    schedule.append((start, end))               # schedule = (始点、終点)

schedule = sorted(schedule, key=lambda x: x[1])
ans = 0
end = -10**12                                   # 始点の最小値

for i in range(M):
    if end <= schedule[i][0]:                   # 重複が OK ならば等号を加える
        end = schedule[i][1]                    # 終点でソートされているので、自動的に可能な中で最速の終点が選ばれている
        ans += 1

print(ans)