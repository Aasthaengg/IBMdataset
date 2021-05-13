def comb_list(n, r, mod):
    ret = [1]
    for i in range(1, r+1):
        ret.append(ret[-1] * (n+1-i) * pow(i, mod-2, mod) % mod)
    return ret

n,k = map(int,input().split())
mod = 10**9+7

r = min(k,n-1)
ans = 0
nCl = comb_list(n, r, mod)
n1Cl = comb_list(n-1, r, mod)

for i in range(r+1):
    ans = (ans + nCl[i] * n1Cl[i]) % mod

print(ans)
