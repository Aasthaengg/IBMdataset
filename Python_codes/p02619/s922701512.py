
# 入力
D = int(input())
C = list(map(int, input().split()))
S_2d = []
for i in range(D):
    s_1d = list(map(int, input().split()))
    S_2d.append(s_1d)
T = []
for i in range(D):
    t = int(input())
    T.append(t)

last_days = [0] * 26
tot_score = 0

for i in range(D):
    today_contest = T[i]
    last_days[today_contest - 1] = i + 1
    today_plus = S_2d[i][today_contest - 1]
    today_minus = 0
    for j, c in enumerate(C):
        today_minus += c * (i + 1 - last_days[j])
    tot_score += today_plus - today_minus
    print(tot_score)

