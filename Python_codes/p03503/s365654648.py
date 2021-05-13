import sys

N = int(sys.stdin.readline().rstrip())

F = [[] for _ in range(N)]
for i in range(N):
    F[i] = list(map(int, sys.stdin.readline().rstrip().split()))

P = []
for i in range(N):
    P.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = -float("inf")
for i in range(1, 1<<10):
    score = 0
    for j in range(N):
        count = 0
        for k in range(10):
            # print(i & (1 << k))
            if i & (1<<k) and F[j][k] == 1:
                count += 1
        # print("count", count)
        score += P[j][count]
    # print(score)
    ans = max(ans, score)

print(ans)