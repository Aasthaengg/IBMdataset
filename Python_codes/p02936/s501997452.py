import sys
sys.setrecursionlimit(10 ** 6)

n,q = map(int,input().split())

#木構造の構築
edges = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

counter = [0]*n
for i in range(q):
    p,x = map(int,input().split())
    counter[p-1] += x#根の部分にカウント

def dfs(now,prev):
    for next in edges[now]:#nowに直接つながる子を順番に参照
        if next == prev: #edgeでは子と親の関係が明示されていないので親につながる情報は無視
            continue
        counter[next] += counter[now]
        dfs(next,now)#行きがかり順にカウント

dfs(0,-1)
print(*counter)

