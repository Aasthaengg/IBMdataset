from collections import Counter
N=int(input())
S=input()
mod = 10**9+7
d = Counter(S)
ans = 1
for v in d.values():
    ans *= v+1
    ans %=mod
print(ans-1)