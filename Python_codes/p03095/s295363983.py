from collections import Counter

n = int(input())
S = input()
counts = Counter(S)
mod = int(1e9) + 7
ans = 1
for count in counts.values():
    ans *= (count + 1)
    ans %= mod
ans -= 1
print(ans)
