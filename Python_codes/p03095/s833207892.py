from collections import Counter

N = int(input())
S = list(input())

ac = Counter(S)
ans = 0
for value in ac.values():
    if ans == 0:
        ans = value+1
    else:
        ans = ans*(value+1)

MOD = 10**9+7
print((ans-1) % MOD)
