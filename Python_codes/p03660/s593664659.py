from collections import deque
n = int(input())
tree = [[] for _ in range(n)]
for _i in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

visit = [-1 for _ in range(n)]
f, s = 0, 0
f_q = deque([0])
s_q = deque([n-1])

while f_q or s_q:
    g = []
    while f_q:
        p = f_q.popleft()
        for i in tree[p]:
            if visit[i] < 0:
                f += 1
                g.append(i)
                visit[i] = 0
    f_q = deque(g)

    g = []
    while s_q:
        p = s_q.popleft()
        for i in tree[p]:
            if visit[i] < 0:
                s += 1
                g.append(i)
                visit[i] = 0
    s_q = deque(g)
if f > s:
    print("Fennec")
else:
    print("Snuke")