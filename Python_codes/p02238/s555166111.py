N = int(input())

Graph = {}
Node_list = []
visited = {}
d = {}
f = {}
t = 1

for i in range(N):
    
    tmp = input().split()
    id = tmp[0]
    Node_list.append(id)
    visited[id] = False

    if int(tmp[1]) != 0:
        Graph[id] = tmp[2:]
    else:
        Graph[id] = []
 


def dfs(node):
    global t

    if visited[node]:
        return

    visited[node] = True

    d[node] = t
    t += 1

    for no in Graph[node]:
        dfs(no)

    f[node] = t
    t += 1

for node in Node_list:
    dfs(node)

for node in Node_list:
    print(node, d[node], f[node])
    
    
    
    
    
    
