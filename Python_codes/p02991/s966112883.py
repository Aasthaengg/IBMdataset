from collections import deque
N, M = map(int, input().split())
R = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    R[a].append(b)
S,T = map(int, input().split())
answer = -1
queue =  deque()
queue.append([S,0])
visited = {}
visited[S] = 1
visited2 = {}
while queue != deque():
    tmp = queue.popleft()
    if tmp[0] == T:
        answer = tmp[1]
        break
    tmp_queue = deque()
    tmp_queue.append(tmp[0])
    for i in range(3):
        tmp2_queue = tmp_queue
        tmp_queue = deque()
        for j in tmp2_queue:
            if (j, i) in visited2:
                continue
            else:
                visited2[j,i] = 1
                tmp_queue += R[j]
    for i in tmp_queue:
        if i in visited:
            continue
        else:
            visited[i] = 1
            queue.append([i,tmp[1]+1])
            
print(answer)