MOD = int(1e9 + 7)
n = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(62):
    cnt = 0
    for a in A:
        if a & 1<<i:
            cnt += 1
    ans += (1<<i % MOD) * cnt % MOD * (n - cnt) % MOD
print(ans % MOD)
