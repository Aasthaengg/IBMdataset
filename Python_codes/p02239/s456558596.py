from collections import deque


def BFS(num):
    color=["white" for _ in range(n+1)]
    D=[-1 for _ in range(n+1)]

    color[num]="gray"
    D[num]=0
    queue=deque([num])

    while len(queue)>0:
        u=queue.popleft()
        for i in M[u]:
            if color[i]=="white":
                color[i]="gray"
                D[i]=D[u]+1
                queue.append(i)
        color[u]="black"

    return D


n=int(input())

M=[[] for _ in range(n+1)]
for i in range(n):
    for j in list(map(int,input().split()))[2:]:
        M[i+1].append(j)

D=BFS(1)
for i in range(1,n+1):
    print(i,D[i])
