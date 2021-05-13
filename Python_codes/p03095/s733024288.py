from collections import Counter

N = int(input())
S = input()
count = Counter(S)
mod = 10**9+7
ans = 1
for k, v in count.items():
    ans = ans * (v+1) % mod
print(ans-1)