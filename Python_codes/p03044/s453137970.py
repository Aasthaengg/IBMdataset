import sys
sys.setrecursionlimit(10 ** 6)


N = int(input())
G = [[] for i in range(N)]

for i in range(N-1):
    a,b,w = map(int,input().split())
    G[a-1].append([b,w])
    G[b-1].append([a,w])
S = [-1]*N

def dfs(x,w,c):
    if w%2 !=0:
        c = 1-c
    S[x]=c
    for i in range(len(G[x])):
        x1 = G[x][i][0]-1
        if S[x1] != -1:
            continue
        w1 = G[x][i][1]
        dfs(x1,w1,c)

dfs(G[0][0][0]-1,G[0][0][1],0)
for i in range(N):
    print(S[i])