# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

'''

区間スケジューリング問題：終点でソートして貪欲法

'''


import sys
input = sys.stdin.readline

N = int(input())
schedule = []
for i in range(N):
    x, l = map(int, input().split())
    schedule.append((x - l, l + x))             # schedule = (始点、終点)

schedule = sorted(schedule, key=lambda x: x[1])
ans = 0
end = -10**12                                   # 始点の最小値

for i in range(N):
    if end <= schedule[i][0]:
        end = schedule[i][1]                    # 終点でソートされているので、自動的に可能な中で最速の終点が選ばれている
        ans += 1

print(ans)