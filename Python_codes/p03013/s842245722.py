n, m = map(int, input().split())
mod = 10**9+7
facs = [1] * (n-m+1)
invs = [1] * (n-m+1)
nfac = 1
for i in range(1, n-m+1):
    nfac = nfac * i % mod
    facs[i] = nfac
    invs[i] = pow(facs[i], mod-2, mod)

ans = 1
start = 0
def steps(start, end):
    t = end - start
    pat = 0
    for j in range(t//2+1):
        pat += (facs[t-j] * invs[j] * invs[t-j-j]) % mod
    return pat%mod

for i in range(m):
    a = int(input())
    end = a-1
    if start == end+1:
        print(0)
        break
    # startからendまで行く方法
    ans *= steps(start, end)
    ans %= mod
    start = a+1
else:
    ans *= steps(start, n)
    ans %= mod
    print(ans)
