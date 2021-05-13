N,M,X = map(int,input().split())
BOOK = [list(map(int,input().split())) for i in range(N)]

costs = []

for i in range(2 ** N):
    t = [0] * M
    cost = 0
    for j in range(N):
        if ((i >> j) & 1) == 1:
            for k in range(M):
                t[k] += BOOK[j][k+1]
            cost += BOOK[j][0]
    
    if all(t[l] >= X for l in range(M)):
        costs.append(cost)

if len(costs) == 0:
    print("-1")
else:
    print(min(costs))