from collections import Counter

MOD = 2019
S = input()
S = tuple(map(int, reversed(S)))
counter = Counter()
digit = 1
cumsum = 0
ans = 0

for i in range(len(S)):
    counter[cumsum] += 1
    cumsum += (S[i] * digit) % MOD
    cumsum %= MOD
    ans += counter[cumsum]
    digit *= 10
    digit %= MOD

print(ans)
