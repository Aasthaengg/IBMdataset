N, T = map(int, input().split())

res = 10 ** 9
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        res = min(res, c)

if res < 10 ** 9:
    print(res)
else:
    print("TLE")
