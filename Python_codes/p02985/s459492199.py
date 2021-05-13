import sys
import collections as col
import numpy as np
MOD = 1000000007
def input():
    return sys.stdin.readline().rstrip()
def main():
    n, k = [int(e) for e in input().split()]
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = [int(e) for e in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    ans = 1
    queue = col.deque([(1, 0, k)])
    while len(queue) > 0:
        u, p, k_ = queue.popleft()
        ans = (ans * k_) % MOD
        if p == 0:
            k_next = k - 1
        else:
            k_next = k - 2
        for v in adj[u]:
            if v == p:
                continue
            queue.append((v, u, k_next))
            k_next -= 1
    print(ans)
main()