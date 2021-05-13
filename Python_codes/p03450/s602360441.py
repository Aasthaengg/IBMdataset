import sys
readline = sys.stdin.readline
read = sys.stdin.read

N, M = map(int, readline().split())

if M == 0:
    print('Yes')
    exit()

LRD = map(int, read().split())
graph = [[] for _ in range(N + 1)]

# 根からの距離、根は複数の可能性あり
distance = [-1] * (N + 1)
child = [0] * (N + 1)

for L, R, D in zip(LRD, LRD, LRD):
    graph[L].append((R, D))
    child[R] = 1

for i in range(1, N + 1):
    if child[i]:
        continue

    # 以下iは根
    distance[i] = 0
    stack = [i]
    while stack:
        V = stack.pop()
        for v, d in graph[V]:
            if distance[v] == -1:
                distance[v] = distance[V] + d
                stack.append(v)
            else:
                if distance[v] != distance[V] + d:
                    print('No')
                    exit()

# 例4のような循環タイプは上のfor内で処理されない
if -1 in set(distance[1:]):
    print('No')
else:
    print('Yes')