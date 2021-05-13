def scoring(last, c, s, t, d, score):
    score += s[d][t[d]-1]
    for i in range(len(c)):
        score -= c[i] * (d+1 - last[d][i])
    return score

score = 0
D = int(input())
c = [int(i) for i in input().split()]
s = []
for i in range(D):
    s.append([int(i) for i in input().split()])
t = []
for i in range(D):
    t.append(int(input()))

last = [[0 for i in range(len(c))] for j in range(D+1)] # last[d][i]

for d in range(D):
    last[d][t[d]-1] = d+1

    for i in range(len(c)):
        last[d+1][i] = last[d][i]

    score = scoring(last, c, s, t, d, score)
    print(score)



