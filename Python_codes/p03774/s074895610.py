n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
c = [list(map(int, input().split())) for j in range(m)]
for k in range(n):
    x = abs(s[k][0] - c[0][0]) + abs(s[k][1] - c[0][1])
    ans = 1
    for l in range(1, m):
        y = abs(s[k][0] - c[l][0]) + abs(s[k][1] - c[l][1])
        if y < x:
            x = y
            ans = l + 1
        elif y == x:
            x = y
    print(ans)