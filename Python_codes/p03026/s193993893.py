import sys
sys.setrecursionlimit(4100000)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
C = list(map(int,input().split()))
C.sort(reverse = True)

D = [0] * N

def dfs(x, parent, index):
    D[x] = C[index]
    index += 1
    for u in edges[x]:
        if u != parent:
            index = dfs(u, x, index)
    return index

dfs(0, -1, 0)

print(sum(C[1:]))
print(*D)