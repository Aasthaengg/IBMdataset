s = input()
x, y = [int(i) for i in input().split(" ")]

xl = []
yl = []

s = s + "T"

xf = True
l = 0
for i in range(0, len(s)):
    if s[i] == "T":
        if xf:
            xl.append(l)
            xf = False
            l = 0
        else:
            yl.append(l)
            xf = True
            l = 0
    else:
        l += 1

x -= xl[0]
xl = xl[1:]

def p(a, l):
    s = sum(a) + l
    if s < 0 or s % 2 == 1:
        return False
    else:
        dp = [[False for j in range(0, s // 2 + 1)] for i in range(0, len(a) + 1)]
        dp[0][0] = True
        for i in range(1, len(a) + 1):
            for j in range(0, s // 2 + 1):
                dp[i][j] = dp[i - 1][j] or (0 <= j - a[i - 1] and dp[i - 1][j - a[i - 1]])
        return dp[len(a)][s // 2]

if p(xl, x) and p(yl, y):
    print("Yes")
else:
    print("No")