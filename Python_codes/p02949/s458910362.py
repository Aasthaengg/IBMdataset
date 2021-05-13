import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
INF = 10**18

def dfs1(cur):
    for to in G1[cur]:
        if done1[to]: continue
        done1[to] = True
        dfs1(to)

def dfs2(cur):
    for to in G2[cur]:
        if done2[to]: continue
        done2[to] = True
        dfs2(to)

N, M, P = map(int, input().split())
G = []
G1 = [[] for i in range(N)]
G2 = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G.append((a, b, c-P))
    G1[a].append(b)
    G2[b].append(a)
D = [0]*N
for i in range(N):
    D[i] = -INF
D[0] = 0
for i in range(N):
    for j in range(M):
        fr, to, cost = G[j]
        if D[fr] != -INF and D[fr]+cost > D[to]:
            D[to] = D[fr]+cost
done1 = [False]*N
done1[0] = True
dfs1(0)
done2 = [False]*N
done2[N-1] = True
dfs2(N-1)
for _ in range(N):
    for j in range(M):
        fr, to, cost = G[j]
        if D[fr] != -INF and D[fr]+cost > D[to]:
            D[to] = D[fr]+cost
            if done1[to] and done2[to]:
                print(-1)
                exit()
if D[N-1] < 0:
    print(0)
else:
    print(D[N-1])
