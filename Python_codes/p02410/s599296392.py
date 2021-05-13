n, m = [int(i) for i in input().split()]

matrix = [[int(i) for i in input().split()] for gyo in range(n)]
vector = [[int(i) for i in input().split()] for gyo in range(m)]

ans = [0 for i in range(n)]


for i in range(n):
    seki = 0
    for j in range(m):
        seki += int(matrix[i][j]) * int(vector[j][0])
    ans[i] = seki


for i in range(len(ans)):
    print(ans[i])