import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]
N = n*(n-1)//2
index = {}
ind = 0
from collections import defaultdict
ns = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        index[i,j] = ind
        index[j,i] = ind
        ind += 1
for i in range(n):
    for j in range(n-2):
        u = index[i,a[i][j]]
        v = index[i,a[i][j+1]]
        ns[u].append(v)
### サイクル検出 cycle detection
seen = [False] * N
done = [False] * N
vals = [None] * N
def dfs(u):
    # uからdfs
    seen[u] = True
    ans = 0
    for v in ns[u]:
        if done[v]:
            ans = max(ans, vals[v]+1)
            continue
        elif seen[v]:
            # サイクルを検出
            return 1
        else:
            pos = dfs(v)
            if pos>=0:
                return 1
            ans = max(ans, vals[v]+1)
    done[u] = True
    vals[u] = ans
    return -1
ans = -float("inf")
for u in range(N):
    if seen[u]:
        continue
    pos = dfs(u)
    if pos>=0:
        print(-1)
        break
else:
    print(max(vals)+1)