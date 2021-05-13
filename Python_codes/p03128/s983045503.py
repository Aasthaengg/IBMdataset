import copy


n,m = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
dict = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
dict2 = {1:1, 2:10**4, 3:10**8, 4:10**12, 5:10**16, 6:10**20, 7:10**24, 8:10**28, 9:10**32}
bonus = 10**36
l = []
for i in a:
    l.append((i,dict[i],dict2[i]))

dp = [[['n',0,[]] for j in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    dp[i][0][0] = "t"
for i in range(1,m+1):
    num = l[i-1][0]
    c = l[i-1][1]
    v = l[i-1][2]
    for j in range(1, n+1):
        if (j-c < 0 or dp[i][j-c][0] == 'n') and dp[i-1][j][0] == 'n':
            continue
        elif (j-c < 0 or dp[i][j-c][0] == 'n'):
            dp[i][j] = copy.copy(dp[i-1][j])
        elif dp[i-1][j][0] == 'n':
            dp[i][j][0] = 't'
            dp[i][j][1] = dp[i][j-c][1] + v + bonus
            dp[i][j][2] = copy.copy(dp[i][j-c][2])
            dp[i][j][2].append(num)
        else:
            dp[i][j][0] = 't'
            if dp[i-1][j][1] >= dp[i][j-c][1]+v+bonus:
                dp[i][j] = copy.copy(dp[i-1][j])
            else:
                dp[i][j][1] = dp[i][j-c][1]+v+bonus
                dp[i][j][2] = copy.copy(dp[i][j-c][2])
                dp[i][j][2].append(num)
L = dp[m][n][2]
L = sorted(L, reverse=True)
ans = ''
for i in range(len(L)):
    ans += str(L[i])
print(int(ans))