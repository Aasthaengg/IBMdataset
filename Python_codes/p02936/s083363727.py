import sys
sys.setrecursionlimit(400000)
N, Q = map(int, input().split())
paths = [list() for _ in range(N+1)] # paths[i] : 頂点iと繋がってる点を全て表す
for _ in range(N-1):
    a, b = map(int, input().split())
    paths[a].append(b)
    paths[b].append(a)
# ab = [list(map(int, input().split())) for _ in range(N-1)]
px = [list(map(int, input().split())) for _ in range(Q)]

ans = [0]*(N+1) # ans[i] : 頂点iについて答える値を格納

counters = [0]*(N+1) # そのノードの部分木に与える点数の総和を格納
for x in px:
    counters[x[0]] += x[1]

visit = [0]*(N+1) #dfsをする時に一度訪れた点に再訪しないための確認
def dfs(node, score, ans):
    visit[node] = 1 # 訪問したことを記録
    score += counters[node] # 自分の部分木に加点する分を加えて後世に残す
    ans[node] = score # 点数の記録
    for loof in paths[node]: # 自分と繋がってる各ノードについて
        if visit[loof] == 0: # まだ探索していなければ
            dfs(loof, score, ans) # 探索

dfs(1, 0, ans)
    

for i in range(1, N+1):
    print(ans[i])