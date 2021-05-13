#写経
#https://atcoder.jp/contests/abc168/submissions/13358850
from collections import deque

def resolve():
    N,M, *AB = map(int, open(0).read().split())
    graph = [[] for _ in range(N+1)]
    for a,b in zip(*[iter(AB)] * 2):
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    signposts = [0] * (N+1)
    signposts[1] = 1
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not signposts[v]:
                signposts[v] = u
                queue.append(v)

    if all(signposts[2:]):
        print("Yes")
        print("\n".join(map(str,signposts[2:])))
    else:
        print("No")
resolve()