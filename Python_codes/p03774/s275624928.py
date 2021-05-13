n, m = [int(x) for x in input().split()]
s_list = [[int(x) for x in input().split()] for _ in range(n)]
c_list = [[int(x) for x in input().split()] for _ in range(m)]
for i in range(n):
    d = 10 ** 9
    p = 0
    for j in range(m):
        temp_d = abs(s_list[i][0] - c_list[j][0]) + abs(s_list[i][1] - c_list[j][1])
        if temp_d < d:
            d = temp_d
            p = j + 1
    print(p)