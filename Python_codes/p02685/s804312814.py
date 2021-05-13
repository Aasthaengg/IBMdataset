MOD = 998244353
n, m, k = map(int, input().split())
c = 1
cnt = 0
for x in range(k + 1):
    cnt += c * m * pow(m - 1, n - 1 - x, MOD) 
    cnt %= MOD
    c *= (n - x - 1) * pow(x + 1, MOD - 2, MOD)
    c %= MOD
print(cnt)