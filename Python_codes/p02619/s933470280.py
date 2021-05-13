D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]


lasts = [[-1] * 26 for _ in range(D + 1)]
S = 0
for d in range(D):
    S += s[d][t[d] - 1]

    for i in range(26):
        if i == t[d] - 1:
            lasts[d+1][i] = d
        else:
            lasts[d+1][i] = lasts[d][i]

    for i in range(26):
        S -= c[i] * (d - lasts[d+1][i])

    print(S)
