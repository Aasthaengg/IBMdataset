import sys
sys.setrecursionlimit(4100000)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
c = list(map(int,input().split()))
L = [0] * N

c.sort(reverse = True)

def dfs(x, par, index):
    L[x] = c[index]
    for u in edges[x]:
        if u != par:
            index += 1
            index = dfs(u, x, index)
    return index

dfs(0, -1, 0)

print(sum(L[1:]))
print(*L)