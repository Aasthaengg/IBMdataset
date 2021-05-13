N, T = map(int, input().split())
min_cost = int(1e9)+11
flg = False
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        flg = True
        min_cost = min(min_cost, c)
if flg:
    print(min_cost)
else:
    print("TLE")