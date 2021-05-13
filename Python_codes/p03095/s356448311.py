from collections import Counter

N = int(input())
S = input()
SC = Counter(S)
mod = 10**9 + 7
ans = 1
for key, value in SC.items():
    ans *= (value+1)
    ans %= mod
print(ans-1)