from collections import deque

def bfs():
    q = deque()
    q.append(1)
    ans = [0] * n
    i = 0
    while q:
        p = q.popleft()
        ans[p - 1] = c[i]
        i += 1
        for j in G[p]:
            if ans[j - 1] == 0:
                q.append(j)
    return ans

n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
c = list(map(int, input().split()))
c.sort(reverse = True)
s = sum(c) - c[0]
ans = bfs()
print(s)
print(*ans)