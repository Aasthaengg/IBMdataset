import sys
sys.setrecursionlimit(10**5)

N, Q = map(int,input().split())
G = [[] for _ in range(N)]
counter = [0] * N

for _ in range(N-1):
    a, b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for _ in range(Q):
    p, x = map(int,input().split())
    counter[p-1] += x

stack, seen = [0], [False]*N
while stack:
    v = stack.pop()
    seen[v] = True

    for u in G[v]:
        if not seen[u]:
            stack.append(u)
            counter[u] += counter[v]

for c in counter:
    print(c, end = " ")
print("")