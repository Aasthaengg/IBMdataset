n = int(input())
adj_path = [[] for _ in range(n)]
paths = []
for _ in range(n-1):
    a,b = map(int,input().split())
    paths.append([a,b])
    adj_path[a-1].append(b-1)
    adj_path[b-1].append(a-1)
c_list = sorted(list(map(int,input().split())),reverse=True)
out = [0 for i in range(n)]
que = [[0,adj_path[0]]]
visited = []
cnt = 0
while(que):
    node_num,children = que.pop(0)
    visited.append(node_num)
    out[node_num] = c_list[cnt]
    cnt += 1
    for child in children:
        if child not in visited:
            que.append([child,adj_path[child]])
score = 0
for path in paths:
    a,b = path
    score += min(out[a-1],out[b-1])
print(score)
print(" ".join(str(x) for x in out))
