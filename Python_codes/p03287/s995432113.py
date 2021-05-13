n, m = map(int, input().split())
a = list(map(int, input().split()))

cum = [0]
for i in range(n):
    cum.append(cum[-1] + a[i])

cum_mod = []
for val in cum:
    cum_mod.append(val % m)

from collections import Counter

ctr = Counter(cum_mod)

ans = 0
for v in ctr.values():
    ans += v*(v-1)//2
print(ans)
