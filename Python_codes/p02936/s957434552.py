import sys
sys.setrecursionlimit(10**7)
n,q=map(int,input().split())
tree=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)
cnt=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x

def DFS(v,p_v):
    for next_v in tree[v]:
        if next_v==p_v:
            continue
        cnt[next_v]+=cnt[v]
        DFS(next_v,v)

DFS(0,-1)
print(*cnt)