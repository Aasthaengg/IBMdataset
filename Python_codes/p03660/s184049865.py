from collections import deque

def BFS_que_tree_2(list_tree,start1,start2,visited):
    visited[start1] = 1
    visited[start2] = -1
    q = deque([[start1,1],[start2,-1]])
    while q:
        start,color  = q.popleft()
        bfs_1step(list_tree,start,visited,q,tag=color)


def bfs_1step(list_tree,start,visited,q,tag=1):
    for node in list_tree[start]:  
        if visited[node] != 0:
            continue
        else:
            visited[node] = tag
            q.append([node,tag])
    return


n = int(input())
tr = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    tr[a-1].append(b-1)
    tr[b-1].append(a-1)

visited = [0]*n
BFS_que_tree_2(tr,0,n-1,visited)
print("Fennec" if sum(visited) > 0 else "Snuke")
