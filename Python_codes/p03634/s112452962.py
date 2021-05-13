import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N = int(input())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

Q, K = map(int, input().split())

d = [-1] * (N + 1)
d[K] = 0
stack = [K]
while stack:
    now = stack.pop()
    for tmp in G[now]:
        next_ = tmp[0]
        if d[next_] == -1:
            d[next_] = d[now] + tmp[1]
            stack.append(next_)

for _ in range(Q):
    x, y = map(int, input().split())
    print (d[x] + d[y])