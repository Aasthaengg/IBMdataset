d = int(input())
C = list(map(int, input().split()))
S = []
for i in range(d):
    S.append(list(map(int, input().split())))
T = [0]
for i in range(d):
    T.append(int(input()))
#print(S)
#print(T)

#最終開催日
Last = [0] * 26

#各Scores
Scores = [0] * 26

for day in range(1, d+1):
    contest = T[day] - 1
    Last[contest] = day
    Scores[contest] += S[day-1][contest]
    for num in range(26):
        Scores[num] -= C[num] * (day - Last[num])
    print(sum(Scores))