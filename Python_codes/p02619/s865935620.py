#入力
D = int(input())
C = [int(c) for c in input().split()]
S = []
for _ in range(D):
    s = [int(x) for x in input().split()]
    S.append(s)
T = []
for _ in range(D):
    t = int(input()) - 1
    T.append(t)
    
#スコア計算
score = 0
last_day = [-1] * 26
for t in range(D):
    test = T[t]
    score += S[t][test]
    last_day[test] = t
    for i in range(26):
        score -= (C[i] * (t - last_day[i]))
    print(score)