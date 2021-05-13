from collections import deque
n,m = map(int,input().split())
data = [[] for _ in range(n)]
hen = []
ans = 0
for _ in range(m):
    v,w = map(int,input().split())
    v -= 1
    w -= 1
    data[v].append(w)
    data[w].append(v)
    hen.append((v,w))
for i,j in hen:
    dq = deque([i])
    visited = [0]*n
    while dq:
        p = dq.pop()
        if p == j:
            break
        visited[p] = 1
        for k in data[p]:
            if (not visited[k]) and (not (p == i and k == j)):
                dq.append(k)
    else:
        ans += 1
print(ans)