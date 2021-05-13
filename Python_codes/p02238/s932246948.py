from sys import stdin
input = stdin.readline

def DFS(node):
    global time
    if discoveredtime[node] == -1:
        discoveredtime[node] = time
        time += 1

        for child in childlist[node]:
            DFS(child)
        
        finishedtime[node] = time
        time += 1

N = int(input())

childlist = [None]*(N+1)
for _ in range(N):
    u, k, *v = map(int, input().split())
    childlist[u] = v

discoveredtime = [-1]*(N+1)
finishedtime = [-1]*(N+1)
time = 1

for i in range(1, N+1):
    if discoveredtime[i] == -1:
        DFS(i)

for i in range(1, N+1):
    print(i, discoveredtime[i], finishedtime[i])
