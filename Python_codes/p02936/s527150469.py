from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

N,Q = map(int, input().split())
neighborlist = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    neighborlist[a].append(b)
    neighborlist[b].append(a)

pointlist = [0]*(N+1)
for _ in range(Q):
    p, x = map(int, input().split())
    pointlist[p] += x

def DFS(v):
    if not checkedlist[v]:
        checkedlist[v] = True
        
        global point
        point += pointlist[v]
        for neighbor in neighborlist[v]:
            DFS(neighbor)
        
        totallist[v] = point
        point -= pointlist[v]
        
totallist = [0]*(N+1)
checkedlist = [False]*(N+1)
point = 0
for i in range(1,N+1):
    if not checkedlist[i]:
        DFS(i)

print(*totallist[1:])