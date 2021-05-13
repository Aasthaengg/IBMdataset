N = list(map(int,input().split()))
Q = [list(map(int,input().split())) for i in range(N[2])]

# N = [4, 6, 10]
# Q = [[2, 4, 1, 86568], [1, 4, 0, 90629], [2, 3, 0, 90310], [3, 4, 1, 29211], [3, 4, 3, 78537], [3, 4, 2, 8580], [1, 2, 1, 96263], [1, 4, 2, 2156], [1, 2, 0, 94325], [1, 4, 3, 94328]]

from itertools import combinations_with_replacement as comb_rplc

C = 0
for seq in comb_rplc(range(1, N[1]+1), N[0]):
    S = 0
    for i in range(N[2]):
        if seq[Q[i][1]-1]-seq[Q[i][0]-1] == Q[i][2]:
            S += Q[i][3]
    if S > C:
        C = S
print(C)