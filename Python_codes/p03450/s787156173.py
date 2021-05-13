from collections import deque
N,M = map(int,input().split())
LRD = []
P = [float('inf') for i in range(N)]
Edges = [[] for i in range(N)]
for i in range(M):
    L,R,D = map(int,input().split())
    L -= 1
    R -= 1
    Edges[R].append((L,-D))
    Edges[L].append((R,D))
for i in range(N):
    Q = deque()
    if P[i] == float('inf'):
        P[i] = 0
        Q.append(i)
    while Q:
        current_pos = Q.popleft()
        for next_pos, d in Edges[current_pos]:
            if P[next_pos] == float('inf'):
                P[next_pos] = P[current_pos] + d
                Q.append(next_pos)
            else:
                if P[next_pos] != P[current_pos] + d:
                    print('No')
                    exit()
print('Yes')