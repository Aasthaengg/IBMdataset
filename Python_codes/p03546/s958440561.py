h,w = map(int,input().split())
cost = []
for _ in range(10):
    c = list(map(int,input().split()))
    cost.append(c)
A = []
for _ in range(h):
    a = list(map(int,input().split()))
    A.append(a)
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])
ans = 0
for a in A:
    for i in a:
        if i != -1:
            ans += cost[i][1]
print(ans)