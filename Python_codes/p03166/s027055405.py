from collections import defaultdict, deque

n, m = map(int, input().split())
xy = []
node = defaultdict(int)
branch = defaultdict(list)
dp = [0]*(n+1) 

for _ in range(m):
    x, y = map(int, input().split())
    xy.append([x, y])
    node[y] += 1 #入り込むノードの数
    branch[x].append(y) # 枝分かれ先


res = []
queue = deque([i for i in range(1, n+1) if node[i]==0])
while queue:
    v = queue.popleft()
    res.append(v)
    
    for u in branch[v]:
        dp[u] = max(dp[u], dp[v]+1)
        node[u] -= 1
        if node[u] == 0:
            queue.append(u)



print(max(dp))