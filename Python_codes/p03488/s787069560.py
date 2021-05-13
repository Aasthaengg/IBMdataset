s = list(input())
x, y = map(int, input().split())
a = [[], []]
b = [0, 0]
j = 0
cnt = 0
for i in s:
    if i == "F":
        if j == 0:
            x -= 1
        else:
            cnt += 1
    else:
        if cnt > 0:
            a[j % 2].append(cnt)
            b[j % 2] += cnt
        j += 1
        cnt = 0
if cnt > 0:
    a[j % 2].append(cnt)
    b[j % 2] += cnt
x, y = abs(x), abs(y)
lx, ly = len(a[0]), len(a[1])
if b[0] < x or b[1] < y:
    print("No")
    exit()
if lx > 0:
    dp = [[0] * (2 * b[0] + 1) for _ in range(lx + 1)]
    dp[0][b[0]] = 1
    for i in range(lx):
        for j in range(2 * b[0] + 1):
            if dp[i][j] == 1:
                dp[i + 1][j + a[0][i]] = 1
                dp[i + 1][j - a[0][i]] = 1
    if dp[lx][b[0] + x] == 0:
        print("No")
        exit()
if ly > 0:
    dp = [[0] * (2 * b[1] + 1) for _ in range(ly + 1)]
    dp[0][b[1]] = 1
    for i in range(ly):
        for j in range(2 * b[1] + 1):
            if dp[i][j] == 1:
                dp[i + 1][j + a[1][i]] = 1
                dp[i + 1][j - a[1][i]] = 1
    if dp[ly][b[1] + y] == 0:
        print("No")
        exit()
print("Yes")