N, M, X = map(int, input().split())
A = list(map(int, input().split()))
cost = [0,0]
for i in range(X, N):
    if i in A:
        cost[0] += 1

for i in range(X, 0, -1):
    if i in A:
        cost[1] += 1

print(min(cost[0],cost[1]))