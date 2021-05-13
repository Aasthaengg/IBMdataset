def scoring(d, t):
    last[t] = d
    return S[d][t] - sum((d - l) * c for l, c in zip(last, C))

D = int(input())
C = list(map(int, input().split()))
S = []
for _ in range(D):
    s = list(map(int, input().split()))
    S.append(s)
T = [int(input()) - 1 for _ in range(D)]
last = [-1] * 26
score = 0
for i in range(D):
    score += scoring(i, T[i])
    print(score)