N, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
#print(graph)

w = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    w[p-1] += x
#print(w)

stack = [0]
flag = [False]*N

while stack:
    next = stack.pop()
    flag[next] = True
    for i in graph[next]:
        if flag[i]:
            continue
        w[i] += w[next]
        stack.append(i)
        #print(stack)

print(" ".join(map(str, w)))