N,C = map(int,input().split())
T = [[0 for i in range(10**5+1)] for j in range(30)]

for i in range(N):
    s,t,c = map(int,input().split())
    T[c-1][s] += 1
    T[c-1][t] -= 1
for i in range(C):
    for j in range(10**5):
        T[i][j+1] += T[i][j]

for i in range(C):
    for j in range(10**5):
        if T[i][-j-1] == 0 and T[i][-j-2] == 1:
            T[i][-j-1] = 1
ans = 0
for i in range(10**5+1):
    ans = max(ans,sum(T[j][i] for j in range(C)))
print(ans)