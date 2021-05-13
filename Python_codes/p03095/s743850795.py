from collections import Counter

n = int(input())
s = input()
mod = 10**9 + 7

c = Counter(s)
ans = 1

for i in range(ord("a"), ord("z")+1):
    ans *= (c[chr(i)] + 1)

print((ans - 1)%mod)