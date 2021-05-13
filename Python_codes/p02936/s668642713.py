import sys
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
X = [0] * N
for _ in range(Q):
    p, x = map(int, sys.stdin.readline().split())
    X[p-1] += x

ans = [0] * N
done = set()
todo = [(0, X[0])]
while todo:
    i, sumx = todo.pop()
    ans[i] = sumx
    done.add(i)
    for ni in G[i]:
        if ni in done:
            continue
        todo.append((ni, sumx + X[ni]))
print(" ".join(map(str, ans)))