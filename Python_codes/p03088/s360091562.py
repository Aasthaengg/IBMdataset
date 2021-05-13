# 末尾3つの塩基配列を4進数で表記して記録する。

def base_10to(n,m):
    if (n//m):
        return base_10to(n//m, m) + str(n%m)
    return str(n%m)


def base_10from(n,m):
    a = 0
    for i in range(len(n)):
        a*=m
        a+=int(n[i])
    return a


n = int(input())

dp = [[0 for i in range(64)] for j in range(n)]


for i in range(64):
    a = base_10to(i,4)
    a= a.zfill(3)
    if a=='012' or a=='102' or a=='021':
        dp[2][i]=0
    else:
        dp[2][i]=1

for i in range(2,n-1):
    for j in range(64):
        a = base_10to(j, 4)
        a = a.zfill(3)
        if a[1:]=='02':
            for k in [0,2,3]:
                dp[i+1][base_10from(a[1:]+str(k),4)] += dp[i][j]
        elif a[1:]=='10' or a[1:]=='01' or a[:2]=='01' or (a[0]=='0' and a[2]=='1'):
            for k in [0,1,3]:
                dp[i+1][base_10from(a[1:]+str(k),4)] += dp[i][j]
        else:
            for k in [0,1,2,3]:
                dp[i+1][base_10from(a[1:]+str(k),4)] += dp[i][j]

print(sum(dp[-1])%(10**9+7))