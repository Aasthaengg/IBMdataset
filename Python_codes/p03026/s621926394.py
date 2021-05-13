from collections import deque

N = int(input())
ab = [[int(i)-1 for i in input().split()] for _ in range(N-1)]
c = [int(i) for i in input().split()]
                
c.sort()
d = [0] * N

vector = [[] for _ in range(N)]
for a, b in ab :
    vector[a].append(b)
    vector[b].append(a)

ret = sum(c[:-1]) 
queue = deque([0])
visited = [False] * N
visited[0] = True

while queue :
    q = queue.popleft()
    for v in vector[q] :
        if not visited[v] :
            queue.append(v)
            visited[v] = True
    d[q] = c.pop()
    
print(ret)
print(' '.join(map(str, d)))