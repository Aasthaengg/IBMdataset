from collections import defaultdict
from collections import deque

N = int(input())

neighbor = defaultdict(dict)

for i in range(N-1):
    a, b, c = map(int, input().split())
    neighbor[a-1][b-1] = c
    neighbor[b-1][a-1] = c

Q, K = map(int, input().split())
K -= 1

dp = [-1] * N

d = deque()
d.append((K, 0, -1))

while d:
    i, cost, parent = d.pop()

    dp[i] = cost

    for j, c in neighbor[i].items():
        if j != parent:
            d.append((j, cost+c, i))

for i in range(Q):
    x, y = map(int, input().split())
    print(dp[x-1] + dp[y-1])
