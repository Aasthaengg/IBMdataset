from collections import deque

N = int(input())

G = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    
C = sorted([int(i) for i in input().split()])

print(sum(C) - max(C))
    
Q = deque()
Q.append(N - 1)
order = []
visited = [False] * N
while len(Q) != 0:
    q = Q.popleft()
    visited[q] = True
    c = C.pop()
    order.append([q, c])
    for g in G[q]:
        if visited[g] == False:
            Q.append(g)

sorted_order = sorted(order)
ans2 = []
for i in range(N):
    ans2.append(sorted_order[i][1])
    
print(' '.join(map(str, ans2)))