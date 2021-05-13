from collections import deque
n = int(input())
a = []
for i in range(n):
    tmp = deque()
    for j in input().split():
        j = int(j)-1
        tmp.append((min(i, j), max(i, j)))
    a.append(tmp)
nxt = []
q = set()
flg = True
for i in range(n):
    t = a[i].popleft()
    if t in q:
        nxt.append(a[t[0]].popleft())
        nxt.append(a[t[1]].popleft())
        q.remove(t)
        flg = False
    else:
        q.add(t)
if flg:
    print(-1)
    exit(0)
ans = 1
while nxt:
    now = nxt[:]
    nxt = []
    flg = True
    for t in now:
        if t in q:
            if a[t[0]]:
                nxt.append(a[t[0]].popleft())
            if a[t[1]]:
                nxt.append(a[t[1]].popleft())
            q.remove(t)
            flg = False
        else:
            q.add(t)
    if flg:
        print(-1)
        exit(0)
    ans += 1
print(ans)