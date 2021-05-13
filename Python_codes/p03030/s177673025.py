N = int(input())
S = []
P = []

for i in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))

name = list(sorted(set(S)))

for i in range(len(name)):
    score = []
    number = []
    for j in range(N):
        if S[j] == name[i]:
            score.append(P[j])
            number.append(j+1)
    for k in range(S.count(name[i])):
        place = score.index(max(score))
        print(number[place])
        del number[place]
        del score[place]
