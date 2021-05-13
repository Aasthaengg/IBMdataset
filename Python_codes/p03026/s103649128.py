from sys import stdin
from collections import defaultdict,deque
N = int(stdin.readline().rstrip())
adj = defaultdict(set)

for i in range(N-1):
    a,b = [int(x) for x in stdin.readline().rstrip().split()]
    adj[a].add(b)
    adj[b].add(a)
    
C = [int(x) for x in stdin.readline().rstrip().split()]

ans = sum(C) - max(C)
print(ans)

visit_p = deque()
visit_p.append(1)
visited = [False]*(N+1)
visited[1] = True

C.sort(reverse=True)
 
print(C[0],end=" ")
cnt = 1
ans_lst = [0]*(N+1)
while visit_p:
    now_v = visit_p.popleft()
    for v in adj[now_v]:
        if visited[v]:
            continue
        ans_lst[v] = C[cnt]
        cnt += 1
        visited[v] = True
        visit_p.append(v)
for i in ans_lst[2:]:
    print(i,end=" ")