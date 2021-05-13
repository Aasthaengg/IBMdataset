from collections import Counter

MOD = 10**9 + 7

N = int(input())
S = input()

c = Counter(S)

ans = 1
for k in c.keys():
    ans *= c[k]+1
    ans %= MOD

ans -= 1

print(ans)
