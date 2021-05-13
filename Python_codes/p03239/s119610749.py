N, T = map(int,input().split())

C = []
for i in range(N):
    c, t = map(int,input().split())
    if t <= T:
        C.append(c)

print('TLE' if len(C) == 0 else min(C))
