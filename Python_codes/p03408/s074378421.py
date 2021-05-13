N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

ans = 0

for s in S:
    point_S = S.count(s)
    point_T = T.count(s)
    ans = max(ans, point_S - point_T)

print(ans)