n, m = map(int, input().split())
c = list(map(int, input().split()))

INF = 10**12

T = [[INF for i in range(n+1)] for j in range(m)]

for i in range(n+1):
    T[0][i] = i

for i in range(m):
    T[i][0] = 0

for i in range(m):
    for j in range(1, n+1):
        if j - c[i] >= 0:
            T[i][j] = min(T[i-1][j], T[i][j - c[i]] + 1)
        else:
            T[i][j] = T[i-1][j]

print(T[m-1][n])