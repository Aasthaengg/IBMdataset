N, T = map(int, input().split())

minCost = float("inf")
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        minCost = min(minCost, c)

if minCost == float("inf"):
    print("TLE")
else:
    print(minCost)
