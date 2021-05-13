n, c = [int(i) for i in input().split()]
D = [[int(i) for i in input().split()] for j in range(c)]
C = [[int(i) for i in input().split()] for j in range(n)]
 
X = [[0]*c for i in range(3)]
 
for i in range(n):
    for j in range(n):
        X[(i+j+2)%3][C[i][j]-1] += 1
 
cost = [[0]*c for i in range(3)]
 
for i in range(c):
    for j in range(c):
        cost[0][j] += X[0][i] * D[i][j]
        cost[1][j] += X[1][i] * D[i][j]
        cost[2][j] += X[2][i] * D[i][j]
 
ans = []
 
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j != k and k != i:
                ans.append(cost[0][i] + cost[1][j] + cost[2][k])
 
print(min(ans))
