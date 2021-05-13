import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((a, b, -c))

inf = 10**18
score = [inf] * (N + 1)
score[1] = 0

for _ in range(N - 1):
    for a, b, c in edge:
        score[b] = min(score[b], score[a] + c)

goal = score[N]
for a, b, c in edge:
    score[b] = min(score[b], score[a] + c)


if goal != score[N]:
    print("inf")
else:
    print(-goal)