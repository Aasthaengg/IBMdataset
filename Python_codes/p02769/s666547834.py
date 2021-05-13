n, k = map(int, input().split())

MOD = int(1e+9+7)

max_zero_num = min(n-1, k)
kai = [1]*(n+1)
gyaku_kai = [1]*(n+1)

for i in range(n):
    kai[i+1] = kai[i]*(i+1) % MOD
    gyaku_kai[i+1] = pow(kai[i+1], MOD-2, MOD)%MOD
        
answer = 0
for zero_num in range(max_zero_num+1):
    answer = (answer + kai[n]*gyaku_kai[n-zero_num]*gyaku_kai[zero_num]*\
    kai[n-1]*gyaku_kai[n-1-zero_num]*gyaku_kai[zero_num]) %MOD

print(answer)
