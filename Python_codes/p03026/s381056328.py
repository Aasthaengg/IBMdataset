from collections import deque

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]
c = sorted(list(map(int, input().split())))

l = [[] for _ in range(n)]
for a, b in ab:
    a, b = a-1, b-1
    l[a].append(b)
    l[b].append(a)
t = [-1]*n
q = deque([0])
w = [0]*n
w[0] = c.pop()
ans = 0
while q:
    v = q.pop()
    for i in l[v]:
        if i == t[v]:
            continue
        t[i] = v
        q.appendleft(i)
        w[i] = c.pop()
        ans += min(w[v], w[i])
print(ans)
print(*w)