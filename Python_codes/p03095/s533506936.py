N = int(input())
S = input()
from collections import Counter
ctr = Counter(S)
MOD = 10**9+7
ans = 1
for v in ctr.values():
    ans *= (v+1)
ans -= 1
print(ans%MOD)