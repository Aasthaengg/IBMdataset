x = [0 for i in range(100001)]
v = [0 for i in range(100001)]
v_sum_right = [0 for i in range(100001)]
v_sum_left = [0 for i in range(100001)]
g = [[0, 0] for i in range(100001)]
g2= [0 for i in range(100001)]
N = 0
C = 0
i = 0
ans = 0
t = 0

N, C = [int(i) for i in input().split(" ")]
for i in range(N):
    x[i], v[i] = [int(i) for i in input().split(" ")]


v_sum_right[0] = v[0]
for i in range(1, N):
    v_sum_right[i] = v_sum_right[i - 1] + v[i]

v_sum_left[N] = 0
for i in range(N - 1, -1, -1):
    v_sum_left[i] = v_sum_left[i + 1] + v[i]


# // g計算
g[0][0] = 0
g[0][1] = 0
g2[0] = 0
for i in range(1, N + 1):
    g[i][0] = max(g[i - 1][0], v_sum_right[i - 1] - x[i - 1])
    g2[i] = max(g2[i - 1], v_sum_right[i - 1] - 2 * x[i - 1])
    if g[i - 1][0] == g[i][0]:
        g[i][1] = g[i - 1][1]
    else:
        g[i][1] = x[i - 1]
    
# // 探査
ans = v_sum_left[0] - C + x[0]
for i in range(1, N):
    ans = max(ans, v_sum_left[i] + g[i][0] - 2 * (C +- x[i]), v_sum_left[i] - C + x[i] + g2[i])
ans = max(ans, g[N][0])

print(ans)