n, m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(m)]

for i in range(m):
    A[i][2] = -A[i][2]

P = [float("inf")] * (n+1)
P[1] = 0
F = [[0] * 2 for i in range(n+1)]
F[1][0] = 1
F[n][1] = 1

for i in range(n):
    for j in range(m):
        if F[A[j][0]][0] == 1 :
            F[A[j][1]][0] = 1
        if F[A[j][1]][1] == 1 :
            F[A[j][0]][1] = 1
        P[A[j][1]] = min(P[A[j][1]], P[A[j][0]] + A[j][2])

ans0 = P[:]

for i in range(1):
    for j in range(m):
        if F[A[j][0]][0] == 1 :
            F[A[j][1]][0] = 1
        if F[A[j][1]][1] == 1 :
            F[A[j][0]][1] = 1
        P[A[j][1]] = min(P[A[j][1]], P[A[j][0]] + A[j][2])

ans1 = P[:]

#print(F)

def d():
    for i in range(n+1):
        if F[i] == [1, 1] and ans1[i] < ans0[i]:
            return "inf"
    return -ans0[n]

print(d())