from collections import deque
num_ver, num_edge = map(int,input().split())
edges_ls = [0] * num_edge
for i in range(num_edge):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edges_ls[i] = [a,b]

num_bridge = 0
for ind_take_edge in range(num_edge):
    graph_ls = [[] for _ in range(num_ver)]
    # graph_lsを作る
    for ind_edge in range(num_edge):
        if ind_edge != ind_take_edge:
            a,b = edges_ls[ind_edge]
            graph_ls[a].append(b)
            graph_ls[b].append(a)
    
    # 0からdfsしてdone_lsを仕上げていく
    done_ls = [0] * num_ver
    queue = deque()
    queue.append(0)
    while queue:
        now = queue.pop()
        done_ls[now] = 1
        for nex in graph_ls[now]:
            if done_ls[nex] != 1:
                queue.append(nex)
    
    if sum(done_ls) != num_ver:
        num_bridge += 1

print(num_bridge)

    

            

