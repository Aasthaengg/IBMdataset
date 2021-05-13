from collections import deque

N = int(input())
tree = [list(map(int, input().split())) for i in range(N-1)]

M = N-1
G = [deque([]) for i in range(N+1)]

for i in range(M):
    G[tree[i][0]].append([tree[i][1], tree[i][2]])
    G[tree[i][1]].append([tree[i][0], tree[i][2]])
    
distance = [-1] * (N+1)     

def dfs(v):
    stack = deque([v])
    distance[v] = 0
    
    while stack:   
        tmp = stack[0]
        if G[tmp]:
            w = G[tmp].popleft() 
            if distance[w[0]] < 0:
                distance[w[0]] = (distance[tmp] + w[1]) % 2
                stack.append(w[0])
        else:
            stack.popleft()
    return distance

distance = dfs(1)
for i in range(N):
    print(distance[i+1])