from collections import deque
n,u,v = map(int,input().split())
branch = [list(map(int,input().split())) for _ in range(n-1)]
link = [[] for _ in range(n)]
for i in branch:
    link[i[0]-1].append(i[1]-1)
    link[i[1]-1].append(i[0]-1)

q_a = deque([u-1])
q_b = deque([v-1])
dist_a = [-1 for _ in range(n)]
dist_b = [-1 for _ in range(n)]
dist_a[u-1] = 0
dist_b[v-1] = 0
while q_a:
    check = q_a.popleft()
    for j in link[check]:
        if dist_a[j] == -1:
            dist_a[j] = dist_a[check]+1
            q_a.append(j)
while q_b:
    check = q_b.popleft()
    for m in link[check]:
        if dist_b[m] == -1:
            dist_b[m] = dist_b[check]+1
            q_b.append(m)

ans = 0
for k in range(n):
    compare = 0
    if dist_b[k]>dist_a[k]:
        compare = dist_b[k]-1

    if compare > ans:
        ans = compare

print(ans)