N, K = map(int, input().split())
mod = 10 ** 9 + 7

inv = [pow(i, mod - 2, mod) for i in range(1, N + 1)]
table = []
inv_table = []
tmp = 1
inv_tmp = 1
for i in range(N):
    tmp *= (i + 1)
    tmp %= mod
    table.append(tmp)
    inv_tmp *= inv[i]
    inv_tmp %= mod
    inv_table.append(inv_tmp)

def cmb(n, k):
    if n == 0:
        return 1
    if k == 0:
        return 1
    if n == k:
        return 1
    ans = table[n - 1]
    ans *= inv_table[k - 1]
    ans *= inv_table[n - k - 1]
    
    return ans % mod
    
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
