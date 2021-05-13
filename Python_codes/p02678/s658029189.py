from collections import deque
n, m = map(int, input().split())

a = [0] * (m + 1)
b = [0] * (m + 1)
road = [[] for _ in range(n + 1)]

for i in range(m):
    a[i], b[i] = map(int, input().split())
    road[a[i]].append(b[i])
    road[b[i]].append(a[i])

ans = [-1] * (n + 1)
ans[0] = 0
ans[1] = 0

q = deque()
q.appendleft(1)

while len(q):
    i = q.pop()
    for j in road[i]:
        if ans[j] == -1:
            ans[j] = i
            q.appendleft(j)

if ans.count(-1) != 0:
    print("No")
    exit()
else:
    print("Yes")
    print(*ans[2:], sep="\n")

