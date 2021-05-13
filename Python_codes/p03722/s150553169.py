import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15

N,M = map(int,input().split())
edge = []
G = [[] for _ in range(N)]
G_inv = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G_inv[b].append(a)
    edge.append((a,b,-c))

can_reach_from_start = [False] * N
can_reach_from_goal = [False] * N
def dfs(i,reach,Gragh):
    for e in Gragh[i]:
        if reach[e]:
            continue
        reach[e] = True
        dfs(e,reach,Gragh)

can_reach_from_start[0] = True
dfs(0,can_reach_from_start,G)
can_reach_from_goal[-1] = True
dfs(N - 1,can_reach_from_goal,G_inv)

X = 0
for i in range(N):
    if can_reach_from_goal[i] and can_reach_from_start[i]:
        X += 1

new_edge = []
for a,b,c in edge:
    if can_reach_from_start[a] and can_reach_from_goal[b]:
        new_edge.append((a,b,c))

def beruman(N,edges,start = 0,negative_loop = False):
    find_negative = False #startを含む負の閉路が存在するか
    dist = [INF] * N
    dist[start] = 0

    for i in range(X):
        update = False
        for a,b,c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                update = True

        if not update:
            break
        if i == X - 1:
            find_negative = True
    
    if negative_loop:
        return dist,find_negative
    else:
        return dist

dist,judge = beruman(N,new_edge,0,True)
if judge:
    print('inf')
else:
    print(-dist[-1])