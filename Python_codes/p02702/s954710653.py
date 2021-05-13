
from collections import defaultdict

S = input()

ctr = defaultdict(int)
ctr[0] = 1
cur = 0
n = len(S)
mod = 2019
for i in reversed(range(n)):
    cur = (cur + int(S[i]) * pow(10, n - i - 1, mod)) % mod
    ctr[cur] += 1

ans = 0
for v in ctr.values():
    ans += v * (v - 1) // 2
print(ans)
