import itertools
N = int(input())
S = [input()[0] for T in range(N)]
MARCH = [S.count('M'),S.count('A'),S.count('R'),S.count('C'),S.count('H')]
Total = 0
for T in itertools.combinations(MARCH,3):
    Total += T[0]*T[1]*T[2]
print(Total)