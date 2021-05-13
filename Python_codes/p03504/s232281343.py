N, C = map(int, input().split())
K = [[0]*(10**5+1) for _ in range(C+1)]
T = [[] for _ in range(C+1)]
for i in range(N):
    s, t, c = map(int, input().split())
    T[c].append([s, t])
    K[c][t] = 1

for i in range(C+1):
    for j in range(len(T[i])):
        s, t = T[i][j]
        if K[i][s] == 0:
            T[i][j][0] -= 0.5
P = [0]*(10**6)
for i in range(C+1):
    for j in range(len(T[i])):
        for k in range(int(2*T[i][j][0]), 2*T[i][j][1]):
            P[k] += 1
print(max(P))
