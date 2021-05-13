import math

N, M = map(int, input().split())
P = [tuple(map(int, input().split())) for i in range(N)]

ans = 0

for i in range(N):
    d = math.sqrt(P[i][0]**2 + P[i][1]**2)
    if d <= M:
        ans += 1

print(ans)
