from collections import deque
N=int(input())
G=[[]for _ in range(N)]
cnt=[0]*N
for i in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    cnt[a]+=1
    cnt[b]+=1

C=list(map(int,input().split()))
C.sort(reverse=True)

root=0
v=0
for i in range(N):
    if v>cnt[i]:
        root=i
        v=cnt[i]

def bfs(s):
    que=deque()
    que.append(s)
    nodes=[-1]*N
    k=0
    ans=0
    while len(que)>0:
        q=que.pop()
        nodes[q]=C[k]
        k+=1

        for v in G[q]:
            if nodes[v]<0:
                que.append(v)
    print(sum(C[1:]))
    print(*nodes)

bfs(root)