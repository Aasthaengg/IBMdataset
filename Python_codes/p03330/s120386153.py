from itertools import permutations
N,Col = map(int,input().split())
D = [[0 for _ in range(Col+1)]]
for _ in range(Col):
    d = list(map(int,input().split()))
    d.insert(0,0)
    D.append(d)
A = [list(map(int,input().split())) for _ in range(N)]
C = {0:{},1:{},2:{}}
for i in range(N):
    for j in range(N):
        c = (i+j)%3
        a = A[i][j]
        if a not in C[c]:
            C[c][a] = 0
        C[c][a] += 1
dmin = 10**10
for x in permutations(range(1,Col+1),3):
    cnt0 = 0
    for c in C[0]:
        cnt0 += C[0][c]*D[c][x[0]]
    cnt1 = 0
    for c in C[1]:
        cnt1 += C[1][c]*D[c][x[1]]
    cnt2 = 0
    for c in C[2]:
        cnt2 += C[2][c]*D[c][x[2]]
    dmin = min(dmin,cnt0+cnt1+cnt2)
print(dmin)