N = int(input())
S = input()
M = 10**9 + 7

from collections import Counter

cs = Counter(S)
ans = 1
for key, val in cs.items():
    ans *= (val + 1)
ans %= M
ans -= 1
print(ans)
