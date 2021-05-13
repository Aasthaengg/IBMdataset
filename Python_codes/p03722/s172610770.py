import sys
input = sys.stdin.buffer.readline
inf = 10 ** 18

N, M = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(M)]

negative = [False] * (N + 1)
cost = [inf] * (N + 1)
cost[1] = 0

for loop in range(N):
    update = False
    for a, b, c in ABC:
        if cost[b] > cost[a] - c:
            cost[b] = cost[a] - c
            if loop == N - 1:
                negative[b] = True

ans = -cost[N]
if negative[N]:
    ans = "inf"
print(ans)
