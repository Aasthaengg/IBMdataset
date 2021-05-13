N, K = map(int, input().split())
mod = 10 ** 9 + 7

def modinv(x):
    return pow(x, mod - 2, mod)

modinv_table = [-1 for _ in range(N + 1)]

for i in range(1, N + 1):
    modinv_table[i] = modinv(i)

def cmb(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans
    
for i in range(1, K + 1): 
    ans = 0
    tmp = cmb(K - 1, i - 1)
    if N - K < i - 1:
        print(ans)
        continue
    else:
        tmp_N = N - K - (i - 1)
        if tmp_N > 0:
            ans += cmb(tmp_N + i, i) * tmp
        else:
            ans += tmp
    print(ans % mod)  