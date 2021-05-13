from collections import deque

N = int(input())
Edge = [[]for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    Edge[b].append((a, c))

Q, K = map(int, input().split())
K -= 1
DP = [-1] * N
DP[K] = 0
A = deque()
A.append((0,K))
while len(A) > 0:
    fatigue, now = A.pop()
    for next, cost in Edge[now]:
        if DP[next] > 0:
            continue
        else:
            DP[next] = fatigue + cost
            A.append((fatigue+cost, next))

for i in range(Q):
    x, y = map(int, input().split())
    print(DP[x-1] + DP[y-1])
