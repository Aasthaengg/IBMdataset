N, T = map(int, input().split())
minC = 10000
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        minC = min(minC, c)
if minC == 10000:
    print("TLE")
else:
    print(minC)
