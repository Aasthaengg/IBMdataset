import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#初期データ、構造
N,Q = (int(x) for x in input().split())
# 隣接リスト表現
connection ={i:set() for i in range(1,N+1)}
for _ in range(N-1):
    a,b = (int(x) for x in input().split())
    connection[a].add(b)
    connection[b].add(a)

point ={i:0 for i in range(1,N+1)}
for _ in range(Q):
    p,x = (int(x) for x in input().split())
    point[p] += x

def DFS(now,prev = -1):
    for next in connection[now]:
        # 親へのエッジはスキップ
        if next == prev:
            continue
        point[next] += point[now] 
        DFS(next,now)

DFS(1)
print(*point.values())
