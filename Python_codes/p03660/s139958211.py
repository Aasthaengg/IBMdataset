from collections import deque

N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dist_from_X(X:int):
    """ BFSで距離を求める """
    dist = [-1] * N
    que = deque([X])
    dist[X] = 0
    while que:
        v = que.popleft()
        for w in edge[v]:
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                que.append(w)
    return dist

Fennec = dist_from_X(0)
Snuke = dist_from_X(N - 1)

# 距離同じ -> Fennec
cntF, cntS = 0,0
for f,s in zip(Fennec, Snuke):
    if f <= s:
        cntF += 1
    else:
        cntS += 1

# cntが同じ -> Snuke
if cntF > cntS:
    print("Fennec")
else:
    print("Snuke")