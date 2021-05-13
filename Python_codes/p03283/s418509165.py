n, m, q = [int(x) for x in input().split()]

t_list = [[0] * (n + 1) for i in range(n + 1)]
c_list = [[0] * (n + 1) for i in range(n + 1)]

for _ in range(m):
    l, r = [int(x) for x in input().split()]
    t_list[l][r] += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        c_list[i][j] = t_list[i][j] + c_list[i][j - 1] + c_list[i - 1][j] - c_list[i - 1][j - 1]

for _ in range(q):
    l, r = [int(x) for x in input().split()]
    print(c_list[r][r] - c_list[l - 1][r] - c_list[r][l - 1] + c_list[l - 1][l - 1])