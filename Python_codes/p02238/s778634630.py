def dfs(v):  # vを訪問する
    global time
    seen[v] = 1
    start[v] = time
    time += 1

    for next_v in graph[v]:
        if seen[next_v]: continue
        dfs(next_v)
    
    end[v] = time
    time += 1


n = int(input())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append([v - 1 for v in line[2:]])

seen = [0] * n  # 0: 未訪問、1: 訪問済
start = [0] * n
end = [0] * n
time = 1

for v in range(n):
    if not seen[v]: dfs(v)

for i in range(n):
    print(i+1, start[i], end[i])

