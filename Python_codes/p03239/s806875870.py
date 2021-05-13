N, T = map(int, input().split())
c_min = 1001
for i in range(N):
    c,t = map(int, input().split())
    if t <= T:
        c_min = min(c, c_min)
if c_min == 1001:
    print("TLE")
else:
    print(c_min)