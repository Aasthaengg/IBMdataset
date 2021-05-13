from collections import Counter
mod = 10 ** 9 + 7
n = int(input())
s = input()
cnt = Counter(s)
ans = 1
for k in cnt.keys():
    ans *= (cnt[k] + 1) % mod
print((ans - 1) % mod)