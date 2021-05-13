n,m,X = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(2**n):
    pat = [0] * n #買うかどうか
    r = [0] * m #理解度
    money = 0
    for j in range(n):
        if ((i>>j)&1):
            pat[n-1-j] = 1
    for x in range(len(pat)):
        if pat[x] == 1:
            money += a[x][0]
            for y in range(m):
                r[y] += a[x][y+1]
    flag = True
    for z in range(m):
        if r[z] < X:
            flag = False
            break
    if flag:
        ans.append(money)
print(min(ans) if ans else -1)