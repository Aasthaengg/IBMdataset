N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
    
points = [0] * N 
for _ in range(Q):
    p, x = map(int, input().split())
    points[p-1] += x

from collections import deque
st = deque([[0, points[0]]])
result = ['0'] * N
visited = [0] * N
visited[0] = 1
while st:
    idx, count = st.pop()
    result[idx] = str(count)
    for ni in G[idx]:
        if visited[ni] != 1:
            visited[ni] = 1
            st.append([ni, count+points[ni]])
            
print(" ".join(result))