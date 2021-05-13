import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())


node = [0 for i in range(N)]
neigh = [[] for j in range(N)]
ans = [0 for i in range(N)]
visited = [0 for i in range(N)]
k = 1

for i in range(N-1):
    ai,bi = map(int,input().split())
    node[ai-1] += 1
    node[bi-1] += 1
    neigh[ai-1].append(bi-1)
    neigh[bi-1].append(ai-1)
c = list(map(int,input().split()))
c.sort(reverse=True)
flag = False
def dfs(neighbor,start):
    global flag
    global k
    if sum(visited) == N:
        return 0

    for i in neighbor[start]:
        
        if visited[i] == 0:
            ans[i] = c[k]
            k += 1
            visited[i] = 1
            try:
                dfs(neighbor,i)
            except RuntimeError:
                flag = True
                return 0




m = max(node)
nn = node.index(m)
#nn = [node[i] for i in range(N) if node[i] == m][0]
visited[nn] = 1
ans[nn] = max(c)

dfs(neigh,nn)
"""
if flag:
    print(100)
    print(' '.join([str(i) for i in range(N)]))
    exit()
"""
ans2 = ' '.join([str(ans[i]) for i in range(N)])


print(sum(c)-max(c))
print(ans2)