D = int(input())
C = [int(x) for x in input().split()]
S = []
for i in range(D):
    S.append([int(x) for x in input().split()])
T = [int(input()) for i in range(D)]


def last(d, i):
    l = 0
    for j in range(1, d + 1):
        if T[j - 1] == i + 1:
            l = j
    return l


score = 0

for d in range(1, 1 + D):
    score += S[d - 1][T[d - 1] - 1] - \
        sum([C[i]*(d - last(d, i)) for i in range(26)])
    print(score)
