N, T = map(int, input().split())
BAD = 10000
min_cost = BAD
for i in range(N):
    c, t = map(int, input().split())
    if t <= T and c < min_cost:
        min_cost = c
if min_cost == BAD:
    print("TLE")
else:
    print(min_cost)
