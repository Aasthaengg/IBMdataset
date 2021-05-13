import sys
sys.setrecursionlimit(100000)

def DFS(i,a,b):
    if i not in done:
        done.append(i)
        for f in g[i]:
            if [i,f]==[a,b] or [i,f]==[b,a]:
                continue
            else:
                DFS(f,a,b)
    else:
        return

N,M=map(int,input().split())
g=[[] for _ in range(N)]
edge=[]
for _ in range(M):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    edge.append([a-1,b-1])

ans=0
for i in range(M):
    done=[]
    DFS(0,edge[i][0],edge[i][1])
    if len(done)<N:
        ans+=1

print(ans)