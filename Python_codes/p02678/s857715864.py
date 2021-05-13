n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _i in range(m)]
 
visit = [-1 for _ in range(n)]
visit[0] = 0
tree = [[] for _ in range(n)]
for a, b in ab:
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
 
from collections import deque
q = deque([0])
while q:
    p = q.popleft()
    for i in tree[p]:
        if visit[i] < 0:
            visit[i] = p
            q.append(i)
if all(i >= 0 for i in visit):
    print("Yes")
    for i in visit[1:]:
        print(i+1)
else:
    print("No")
