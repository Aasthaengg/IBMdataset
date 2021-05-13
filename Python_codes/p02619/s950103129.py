""" スコア計算機 """

contest_types = 26
days = int(input())
cs = list(map(int, input().strip().split()))
ss = [list(map(int, input().strip().split())) for _ in range(days)]
ts = [int(input()) - 1 for _ in range(days)]

# 満足度
satisfaction = 0

last_days = [-1] * contest_types

for d in range(days):
    # d日目の満足度の増加
    c_type = ts[d]
    increase = ss[d][c_type]
    satisfaction += increase

    # 開催日の更新
    last_days[c_type] = d

    # d日目の満足度の減少
    for i in range(contest_types):
        last = last_days[i]
        decrease = cs[i] * (d - last)
        satisfaction -= decrease

    print(satisfaction)
