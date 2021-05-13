import sys
sys.setrecursionlimit(10**7)

N,Q = map(int,input().split())
tree = [[] for _ in range(N)]

# tree[i]: i番目の頂点とつながっている頂点（リスト）を入れる
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

# x_list[i]: iの配下に足す数を入れる
x_list = [0]*N
for _ in range(Q):
    p,x = map(int,input().split())
    x_list[p-1] += x

ans = [0]*N

def dfs(child, parent):
    ans[child] = ans[parent] + x_list[child]
    for v in tree[child]:
        if v != parent:
            dfs(v, child)

dfs(0,0)
print(' '.join([str(i) for i in ans]))