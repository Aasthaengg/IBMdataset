n, c_max = map(int, input().split())
D = []
for _ in range(c_max):
    d = list(map(int, input().split()))
    D.append(d)
C = []
for _ in range(n):
    c = list(map(int, input().split()))
    C.append(c)

Res = [[] for _ in range(3)]
\
for i in range(n):
    for j in range(n):
        now = C[i][j]
        if (i+j) % 3 == 0:
            Res[0].append(now)
        elif (i+j) % 3 == 1:
            Res[1].append(now)
        else:
            Res[2].append(now)

Res_cost = [[0 for _ in range(c_max)] for _ in range(3)]

for i in range(3):    
    for color in range(c_max):
        cost = 0
        for now in Res[i]:
            cost += D[now-1][color-1]
        Res_cost[i][color-1] = cost

ans = 10**10
for i in range(c_max):
    for j in range(c_max):
        for k in range(c_max):
            if i == j or j == k or k == i:
                continue
            cost = Res_cost[0][i] + Res_cost[1][j] + Res_cost[2][k]
            ans = min(cost, ans)
# print(Res_cost)
# print(Res)
print(ans)   