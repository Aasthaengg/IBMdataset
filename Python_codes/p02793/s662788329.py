from collections import Counter

mod = 10**9 +7
N = int(input())
A = list(map(int,input().split()))

lcm = Counter([])
for a in A:
    tmp = []
    d = 2
    while d*d <= a:
        while a%d == 0:
            tmp.append(d)
            a //= d
        d += 1
    if a != 1:
        tmp.append(a)
    tmp = Counter(tmp)
    for k,v in tmp.items():
        if k not in lcm or v > lcm[k]:
            lcm[k] = v

LCM = 1
for k,v in lcm.items():
    LCM = LCM * pow(k,v,mod) % mod

ans = 0
for a in A:
    ans += LCM * pow(a,mod-2,mod) % mod
    ans %= mod

print(ans)

