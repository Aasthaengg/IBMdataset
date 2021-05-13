from collections import Counter
n = int(input().rstrip())
c = Counter(input().rstrip())
MOD = 10**9+7

ans = 1
for v in c.values():
    ans *= v+1
    ans %= MOD

print(ans-1)