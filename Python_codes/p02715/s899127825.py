MOD = 1000000007

n, k = map(int, input().split())
ans = [0 for i in range(k+1)]
for i in range(k,0,-1):
    t = 0
    for j in range(2*i, k+1, i):
        t = (t + ans[j]) % MOD
    ans[i] = (pow(k//i, n, MOD) - t + MOD) % MOD
sm = 0
for i in range(1, k+1):
    sm = (sm + (i*ans[i]) % MOD) % MOD
print(sm % MOD)
