from collections import Counter

N = int(input())
A = list(map(int,input().split()))
mod = 10**9 +7

divide = []
for a in A:
    tmp = []
    d = 2
    while d*d <= a:
        while a % d == 0:
            a //= d
            tmp.append(d)
        d += 1
    if a != 1:
        tmp.append(a)
    divide.append(Counter(tmp))

count = Counter([])
for d in divide:
    for k,v in d.items():
        if k not in count:
            count[k] = v
        else:
            count[k] = max(count[k],v)

LCM = 1
for k,v in count.items():
    LCM *= pow(k,v,mod)
    LCM %= mod

ans = 0
for a in A:
    ans += LCM*pow(a,mod-2,mod)
    ans %= mod
print(ans)