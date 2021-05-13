from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)

def DFS(node):
    if not checked[node]:
        global point
        checked[node] = True
        point += pointlist[node]
        
        for child in neighborlist[node]:
            if not checked[child]:
                DFS(child)
        
        anslist[node] += point
        point -= pointlist[node]

N,Q = map(int, input().split())
neighborlist = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    neighborlist[a].append(b)
    neighborlist[b].append(a)

pointlist = [0]*(N+1)
for _ in range(Q):
    p,x = map(int, input().split())
    pointlist[p] += x

checked = [False]*(N+1)
anslist = [0]*(N+1)
point = 0

DFS(1)

print(*anslist[1:])