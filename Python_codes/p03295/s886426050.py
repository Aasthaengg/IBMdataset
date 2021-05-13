def Schedule(schedule):
    """
    :return: 複数の区間が与えられた時の重複の無い区間の選び方の最大数
    """
    schedule = sorted(schedule, key=lambda x: x[1])
    N = len(schedule)
    res = 0
    end = -float("inf")

    for i in range(N):
        if end <= schedule[i][0]:  # 重複がダメならば等号を消す
            end = schedule[i][1]  # 終点でソートされているので、自動的に可能な中で最速の終点が選ばれている
            res += 1
    return res

################################################################################

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
schedule = []
for i in range(M):
    start, end = map(int, input().split())
    schedule.append((start, end))               # schedule = (始点、終点)

print(Schedule(schedule))