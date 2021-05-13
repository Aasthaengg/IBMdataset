N, M = map(int, input().split())

lower = 0
upper = N+1
for _ in range(M):
    L, R = map(int, input().split())
    lower = max(lower, L)
    upper = min(upper, R+1)
c = upper - lower
if c <= 0:
    print(0)
else:
    print(c)
