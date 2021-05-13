from collections import Counter

N = int(input())
S = input()

MOD = 10**9 + 7
cnt = Counter(S)
ans = 1
for i in cnt.values():
    ans *= (i + 1)
    ans %= MOD
print(ans-1)
