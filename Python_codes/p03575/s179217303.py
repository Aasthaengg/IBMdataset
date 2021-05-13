from collections import deque

def check(st,en,ed):
    ed[st-1][en-1] -= 1
    ed[en-1][st-1] -= 1
    cnt = [0] * n
    q = deque()
    q.append(st)
    cnt[st-1] += 1
    while q:
        now = q.popleft()
        if ed[now-1][en-1] == 1:
            ed[st-1][en-1] += 1
            ed[en-1][st-1] += 1
            return False
        for r in range(n):
            if ed[now-1][r] == 1 and cnt[r] == 0:
                q.append(r+1)
                cnt[r] += 1
    ed[st-1][en-1] += 1
    ed[en-1][st-1] += 1
    return True

n, m = map(int, input().split())

edge = [[0] * n for _ in range(n)] 

nodes = []

for i in range(m):
    a, b = map(int, input().split())
    nodes.append((a,b))
    edge[a-1][b-1] += 1
    edge[b-1][a-1] += 1

ans = 0 
for node in nodes:
    a,b = node[0], node[1]
    if check(a,b,edge):
        ans += 1

print(ans)