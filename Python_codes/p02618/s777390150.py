# 貪欲の評価関数を選ぶ
d = int(input())
dd = d * (d + 1) // 2
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]


def calc_score(T):
    L = [-1 for j in range(26)]
    X = [0 for j in range(26)]
    score = 0
    for i in range(d):
        score += S[i][T[i]]
        X[T[i]] += (d - i) * (i - L[T[i]])
        L[T[i]] = i
    for j in range(26):
        score -= C[j] * (dd - X[j])
    return score


max_score = -10**8
best_T = [0 for i in range(26)]
for next_day in range(26):
    T = []
    L = [-1 for j in range(26)]
    for i in range(d):
        max_diff = -10**7
        best_j = 0
        for j in range(26):
            memo = L[j]
            L[j] = i
            diff = S[i][j] - sum([C[k] * (min(i + next_day, d) - L[k])
                                  for k in range(26)])
            if diff > max_diff:
                max_diff = diff
                best_j = j
            L[j] = memo
        T.append(best_j)
        L[best_j] = i
    score = calc_score(T)
    if score > max_score:
        max_score = score
        best_T = T
for t in best_T:
    print(t + 1)
