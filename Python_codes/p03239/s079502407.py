N, T = map(int, input().split())
min_cost = 10**9
for i in range(N):
    c, t = map(int, input().split())
    if t > T:
        continue
    else:
        min_cost = min(min_cost, c)
if min_cost != 10**9:
    print(min_cost)
else:
    print("TLE")
