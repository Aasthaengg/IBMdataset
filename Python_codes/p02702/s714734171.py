from collections import defaultdict
S = input()[::-1]
mod = 2019
d = defaultdict(int)
ruijo = 1
tmp = 0
for i in range(len(S)):
    tmp += int(S[i]) * ruijo % mod
    d[tmp % mod] += 1
    ruijo *= 10
    ruijo %= mod
ans = 0
for k, v in d.items():
    ans += v * (v - 1) // 2
    if k == 0:
        ans += v
print(ans)