from collections import deque
N = int(input())
es = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    es[a].append(b)
    es[b].append(a)
c = list(map(int, input().split()))
c.sort(reverse=1)
q = deque()
q.append(0)
flg = [0]*N
num = [None]*N
i = 0
while len(q):
    v = q.popleft()
    flg[v] = 1
    num[v] = c[i]
    i += 1
    for u in es[v]:
        if flg[u]:
            continue
        q.append(u)
print(sum(c[1:]))
print(*num)


