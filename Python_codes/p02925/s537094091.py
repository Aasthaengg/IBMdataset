# BFS的にやるDAGの最長経路
from collections import deque
import copy
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n=int(input())
a= [list(map(int, input().split())) for i in range(n)]
v=n*(n-1)//2
# 試合を格納
b=[[] for i in range(v)]
# 入次数を記録
indeg = [0 for _ in range(v)]

for i in range(n):
    for j in range(n-1):
        # i+1<a[i][j]で統一
        if i+1>a[i][j]:
            x=a[i][j]
            y=i+1
        else:
            x=i+1
            y=a[i][j]
        # 試合を頂点に変換
        a[i][j]=(n-1+n-x+1)*(x-1)//2+y-x-1
    for j in range(n-2):
        indeg[a[i][j+1]]+=1
        b[a[i][j]].append(a[i][j+1])

dp = [0 for _ in range(v)]
q = deque([])
# 最長辺の候補を入れる
for i in range(v):
    if indeg[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    for w in b[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            q.append(w)
            dp[w] = max(dp[w], dp[v] + 1)

# indegが全てゼロになってなければ閉路あり
if sum(indeg)!=0:
    print(-1)
else:
    # 最長経路
    print(max(dp)+1)
