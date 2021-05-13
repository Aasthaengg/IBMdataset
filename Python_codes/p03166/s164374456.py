from collections import defaultdict, deque

n,m = map(int,input().split())
edge = []
for _ in range(m):
    x,y = map(int,input().split())
    edge.append((x,y))

in_cnt = defaultdict(int)
outs = defaultdict(list)
for x,y in edge:
    in_cnt[y-1]+= 1
    outs[x-1].append(y-1)

res = []
queue = deque([i for i in range(n) if in_cnt[i] == 0])

while  len(queue)> 0:
    node = queue.popleft()
    res.append(node)
    for next_node in outs[node]:
        in_cnt[next_node] -= 1
        if in_cnt[next_node] == 0:
            queue.append(next_node)

dp = [0]*n

for i in range(n):
    for nv in outs[res[i]]:
        dp[nv] =max(dp[nv],dp[res[i]] + 1)
print(max(dp))