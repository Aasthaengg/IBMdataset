# input
N, K = map(int, input().split())

MOD = 10**9+7

# process
l = [0]*(K+1)  # 最大公約数がiとなる数列の数
ans = 0
for i in range(K, 0, -1):
    l[i] = pow((K//i), N, MOD) - sum(l[i*j] for j in range(2, K//i+1)) % MOD
    ans = (ans + i*l[i]) % MOD

# output
print(ans)
