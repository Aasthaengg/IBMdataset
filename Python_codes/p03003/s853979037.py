import copy
n,m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
dp = [0 for i in range(max(n,m))]
mod = 10**9+7
if n > m:
    a = s
    b = t
else:
    a = t
    b = s
    c = copy.copy(n)
    n = copy.copy(m)
    m = copy.copy(c)
l = []
for i in range(m):
    now = b[i]
    bl = []
    for j in range(n):
        if now == a[j]:
            bl.append(j)
    l.append(bl)
for i in range(m):
    if len(l[i]) > 0:
        dp2 = copy.copy(dp)
        now1 = 0
        k = 0
        k1 = len(l[i])
        count = 0
        while k < k1:
            if now1 == l[i][k]:
                dp[now1] += 1
                dp[now1] += count
                dp[now1] %= mod
                k += 1
            count += dp2[now1]
            count %= mod
            now1 += 1
        #print(dp)
print((sum(dp)+1)%mod)