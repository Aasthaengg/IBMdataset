from collections import deque
N, K = map(int, input().split())
tree = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

depth = [-1]*N
mod = 10**9+7

# WFS
next_v = deque([0])
depth[0] = 0
ans = K
while next_v:
    s = next_v.popleft()
    color = max(K-depth[s]-1, K-2)

    for t in tree[s]:
        if depth[t] != -1:
            continue
        next_v.append(t)
        depth[t] = depth[s] + 1

        ans *= color
        ans %= mod
        color -= 1

print(ans)
