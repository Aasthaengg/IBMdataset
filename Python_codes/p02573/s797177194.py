from collections import deque
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
t = dict()
for i in range(1, n+1):
    t[i] = set()
for a, b in ab:
    t[a].add(b)
    t[b].add(a)

q = deque()
s = set()
ans = 0
for i in range(1, n+1):
    if i not in s:
        q.append(i)
        s.add(i)
        tmp = [i]
        while q:
            v = q.popleft()
            for ti in t[v]:
                if ti not in s:
                    tmp.append(ti)
                    q.append(ti)
                    s.add(ti)
    ans = max(ans, len(tmp))
print(ans)
