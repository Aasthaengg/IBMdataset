n,a,b = map(int, input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)

mx=-1
for i in range(a,b+1):
    mx = max(mx,sum(v[:i])/i)
print(mx)

def modinv(a, mod=10**24+7):
    return pow(a, mod-2, mod)

def comb(n, r, mod=10**24+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

import collections
c = collections.Counter(v)
ans=0
for i in range(a,b+1):
    if sum(v[:i])/i == mx:
        cnt=1

        c2 = collections.Counter(v[:i])

        for itm in c2.items():
            base_cnt = c[itm[0]]
            cnt*=comb(base_cnt,itm[1])
        ans+=cnt

print(ans)