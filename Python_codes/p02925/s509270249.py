import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]
N = n*(n-1)//2
index = [[0]*(n) for i in range(n)]
ind = 0
from collections import defaultdict
ns = [[] for _ in range(N)]
for i in range(n):
    for j in range(i+1,n):
        index[i][j] = ind
        index[j][i] = ind
        ind += 1
for i in range(n):
    for j in range(n-2):
        u = index[i][a[i][j]]
        v = index[i][a[i][j+1]]
        ns[u].append(v)
### サイクル検出 cycle detection
seen = [False] * N
done = [False] * N
vals = [None] * N
def dfs(u):
    s = [u]
    while s:
        u = s.pop()
        if u>=0:
            # 非負の値: 新しい頂点に到達
            seen[u] = True
            s.append(~u)
            for v in ns[u]:
                if done[v]:
                    continue
                elif not seen[v]:
                    s.append(v)
                else:
                    # 閉路発見
                    return True
        else:
            u = ~u
            done[u] = True
            # ここに帰りがけ処理を書く
            val = 0
            for v in ns[u]:
                # uの子はすべて処理が終わっている
                val = max(val, vals[v]+1)
            vals[u] = val
    return False

ans = -float("inf")
for u in range(N):
    if seen[u]:
        continue
    pos = dfs(u)
    if pos:
        print(-1)
        break
else:
    print(max(vals)+1)