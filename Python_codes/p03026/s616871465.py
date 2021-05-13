import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
clst = list(map(int, input().split()))
clst.sort(reverse = True)
ans = [0 for _ in range(n)]
ind = 0
total = 0
def dfs(pos, b_pos, b_num):
    global ind, total
    ans[pos] = clst[ind]
    total += min(ans[pos], b_num)
    ind += 1
    for n_pos in edges[pos]:
        if n_pos == b_pos:
            continue
        dfs(n_pos, pos, ans[pos])
        
dfs(0, -1, 0)
print(total)
print(*ans)