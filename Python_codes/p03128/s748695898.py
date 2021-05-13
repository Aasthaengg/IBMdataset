n, m = map(int, input().split())
a = list(map(int, input().split()))

c = [0] * 8

mt = set()
for aa in a:
    if aa == 1:
        c[2] = 1
        mt.add(2)
    if aa == 2:
        c[5] = max(c[5], 2)
        mt.add(5)
    if aa == 3:
        c[5] = max(c[5], 3)
        mt.add(5)
    if aa == 4:
        c[4] = 4
        mt.add(4)
    if aa == 5:
        c[5] = max(c[5], 5)
        mt.add(5)
    if aa == 6:
        c[6] = max(c[6], 6)
        mt.add(6)
    if aa == 7:
        c[3] = 7
        mt.add(3)
    if aa == 8:
        c[7] = 8
        mt.add(7)
    if aa == 9:
        c[6] = max(c[6], 9)
        mt.add(6)
dp = [-1] * (n+1)
dp[0] = 0
for i in range(n+1):
    tmp = [dp[i]]
    for mtt in mt:
        if i-mtt>= 0 and dp[i-mtt] >= 0:
            tmp.append(dp[i-mtt]*10+c[mtt])
    dp[i] = max(tmp)
print(dp[n])