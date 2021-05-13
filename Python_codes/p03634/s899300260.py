import sys
input = sys.stdin.readline
N = int(input())

g = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
    
Q, K = map(int, input().split())

cost = [-1] * (N+1)
cost[K] = 0
temp = [K]
while temp:
    p = temp.pop()
    for q in g[p]:
        if cost[q[0]] == -1:
            cost[q[0]] = cost[p] + q[1]
            temp.append(q[0])

for i in range(Q):
    x, y = map(int, input().split())
    print(cost[x] + cost[y])
