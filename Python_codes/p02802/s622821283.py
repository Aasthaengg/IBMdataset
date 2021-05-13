n,m = map(int,input().split())
lis = [list(input().split()) for _ in range(m)]

dp = [[0 for _ in range(2)] for _ in range(n)] # AC_flg, WA数

for i in range(m):
    if dp[int(lis[i][0])-1][0]==1:
        continue
    else:
        if lis[i][1]=='WA':
            dp[int(lis[i][0])-1][1] += 1
        if lis[i][1]=='AC':
            dp[int(lis[i][0])-1][0] = 1

ac = 0
wa = 0

for i in range(n):
    if dp[i][0]==1:
        ac += 1
        wa += dp[i][1]

print(ac,wa)