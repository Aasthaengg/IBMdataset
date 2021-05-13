# 点数計算
def scoring(last_, c, s, t, d, score):
    # score += s[d][t[d]-1]
    score = s[d][t]
    k = 8
    
    for i in range(len(c)):
        # score -= c[i] * (d+1 - last_[d][i])
        # score -= c[i] * (d + 1 - last_[i])
        score -= k * c[i] * (d - last_[i]) + c[i] * (k * (k+1)) / 2
    return score


# input
D = int(input())
c = [int(i) for i in input().split()]
s = []
for i in range(D):
    s.append([int(i) for i in input().split()])
# t = []
# for i in range(D):
#     t.append(int(input()))
last = [[0 for i in range(len(c))] for j in range(D+1)] # last[d][i]

ans = []
for d in range(D):
    # last[d][t[d]-1] = d+1
    last_dummy = last[d][:]
    score = -float("inf")
    t_d = 0
    for t in range(len(c)):
        last_dummy2 = last_dummy[:]
        last_dummy2[t] = d+1
        if score < scoring(last_dummy2, c, s, t, d, score):
            score = scoring(last_dummy2, c, s, t, d, score)

            t_d = t

    ans.append(t_d)
    last[d][t_d] = d+1


    # last更新
    for i in range(len(c)):
        last[d+1][i] = last[d][i]


[print(ans[i]+1) for i in range(D)]



