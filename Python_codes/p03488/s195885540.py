
def YesNo(b):
    print("Yes" if b else "No")


def solve(v, l, ini):
    ml = 8000*2+1
    dp = [[False]*ml for i in range(len(l)+1)]
    for i in range(len(ini)):
        dp[0][ini[i]+8000] = True
    for i in range(1, len(l)+1):
        for j in range(ml):
            if (j+l[i-1]) < ml and dp[i-1][j]:
                dp[i][j+l[i-1]] = True
            if (j-l[i-1]) >= 0 and dp[i-1][j]:
                dp[i][j-l[i-1]] = True
    return dp[len(l)][v+8000]


s = input()
x, y = map(int, input().split())
si = 0
while si < len(s) and s[si] == 'F':
    si += 1

s = s[si:]
if len(s) == 0:
    YesNo(x == si and y == 0)
else:
    f = s.split('T')[1:]
    xl, yl = [0], [0]
    for i in range(len(f)):
        if len(f[i]) == 0:
            continue
        if i % 2 == 0:
            yl.append(len(f[i]))
        else:
            xl.append(len(f[i]))

    YesNo(solve(x, xl, [si]) and solve(y, yl[1:], [-yl[0], yl[0]]))
