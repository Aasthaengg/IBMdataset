N, K = map(int, input().split())
x_list = []
y_list = []
xy_list = []
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    xy_list.append((x, y))
x_dict = {}
x_dict_rev = {}
y_dict = {}
y_dict_rev = {}
x_list.sort()
y_list.sort()
for i, xi in enumerate(x_list):
    x_dict[xi] = i
    x_dict_rev[i] = xi
for i, yi in enumerate(y_list):
    y_dict[yi] = i
    y_dict_rev[i] = yi
xy_c = [[0 for _ in range(N)] for _ in range(N)]
for x, y in xy_list:
    xy_c[x_dict[x]][y_dict[y]] = 1

cs = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        cs[i+1][j+1] = cs[i+1][j] + cs[i][j+1] - cs[i][j] + xy_c[i][j]

ans = float('inf')
for x_min in range(1, N+1):
    for x_max in range(1, N+1):
        for y_min in range(1, N+1):
            for y_max in range(1, N+1):
                if cs[x_max][y_max] - cs[x_min-1][y_max] - cs[x_max][y_min-1] + cs[x_min-1][y_min-1] >= K:
                    ans = min(ans, (x_dict_rev[x_max-1] - x_dict_rev[x_min-1]) * (y_dict_rev[y_max-1] - y_dict_rev[y_min-1]))


print(ans)
