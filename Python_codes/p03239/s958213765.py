N, T = map(int, input().split())
c_t = [list(map(int, input().split())) for _ in range(N)]
cost = 2000000
TLE_flg = True
for i in range(N):
    if c_t[i][1] <= T:
        cost = min(cost, c_t[i][0])
        TLE_flg = False
print('TLE' if TLE_flg else cost)
