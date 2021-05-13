N, T = map(int, input().split())
D = []
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        D.append(c)
if D:
    print(min(D))
else:
    print("TLE")