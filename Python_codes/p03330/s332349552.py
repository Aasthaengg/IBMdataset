n, c = map(int, input().split())
dl = []
for i in range(c):
    dl.append(list(map(int, input().split())))
cl = []
for i in range(n):
    cl.append(list(map(int, input().split())))

d = {i: [0]*c for i in range(3)}

for i in range(n):
    for j in range(n):
        d[(i+j)%3][int(cl[i][j])-1] += 1
cost = {i: [0]*c for i in range(3)}
for i in range(3):
    for j in range(c):
        for k in range(c):
            cost[i][j] += int(dl[k][j]) * d[i][k]
ans = float('inf')
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j !=k and k != i:
                ans = min(ans, cost[0][i]+cost[1][j]+cost[2][k])
print(ans)
        
