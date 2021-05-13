import sys
from collections import deque

readline = sys.stdin.buffer.readline
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))

def solve():
    mod = 10**9 + 7
    n, k = nm()
    G = [list() for _ in range(n)]
    ans = 1
    for _ in range(n-1):
        u, v = nm()
        u -= 1; v -= 1
        G[u].append(v)
        G[v].append(u)
    q = deque()
    chi = [0]*n
    par = [-1]*n
    q.append(0)
    while q:
        v = q.popleft()
        c = k - chi[par[v]]
        if par[v] >= 0:
            chi[par[v]] += 1
            c -= 1
            if par[par[v]] >= 0:
                c -= 1
        ans = ans * c % mod
        for x in G[v]:
            if x != par[v]:
                par[x] = v
                q.append(x)
    print(ans)
    return

solve()

# T = ni()
# for _ in range(T):
#     solve()
