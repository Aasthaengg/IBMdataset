from collections import Counter
N=int(input())
S=input()
mod = 10**9+7
d = Counter(S)
ans = 0
for i in S:
    tmp = 1
    d[i] -=1
    for k,v in d.items():
        if i!=k and v:
            tmp *=(v+1)
            tmp%=mod
    ans += tmp
    ans %=mod
print(ans)