n, m, x, y = map(int,input().split())

x_n = list(map(int,input().split()))
y_m = list(map(int,input().split()))

x_n_max = max(x_n)
y_m_min = min(y_m)


if x > y:
    x_n_max = 1000000000000000000000

ans = 0
for z in range(x+1,y+1):
    if x_n_max < z and y_m_min >= z:
        print('No War')
        ans = -1
        break


if ans == 0:
    print('War')