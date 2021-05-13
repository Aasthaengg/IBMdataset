"""
何回も再帰するときはlimitを増やす
dfs
"""
import sys
sys.setrecursionlimit(200000)

n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(m)]


tree = [[] for _ in range(n)]
for a,b in l:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

bit = [0 for _ in range(n)]
def dfs(v):
    bit[v] = 1
    for j in tree[v]:
        if bit[j]==0:
            dfs(j)

ans = 0
for i in range(m):
    a,b = l[i]
    a -= 1
    b -= 1
    tree[a].remove(b)
    tree[b].remove(a)
    bit = [0 for _ in range(n)]
    dfs(a)
    if bit.count(1) !=n:
        ans += 1

    tree[a].append(b)
    tree[b].append(a)
print(ans)

