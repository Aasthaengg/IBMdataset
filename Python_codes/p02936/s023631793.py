N,Q = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

value_list = [0]*(N+1)

for _ in range(Q):
    p,x = map(int,input().split())
    value_list[p] += x 


from  collections import deque

que = deque([(0,1)])

while que:
    parent,me = que.popleft()
    value_list[me]+=value_list[parent]
    for child in graph[me]:
        if child==parent:
            continue
        else:
            que.append((me,child))


print(*value_list[1:])