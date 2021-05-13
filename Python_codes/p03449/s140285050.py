n = int(input())
a_list = [[int(x) for x in input().split()] for _ in range(2)]
a_c_list = [[0] * (n + 1), [0] * (n + 1)]
for i in range(2):
    for j in range(1, n + 1):
        a_c_list[i][j] = a_list[i][j - 1] + a_c_list[i][j - 1]
ans = 0
for i in range(1, n + 1):
    temp = a_c_list[0][i] + (a_c_list[1][n] - a_c_list[1][i - 1])
    if temp > ans:
        ans = temp
print(ans)