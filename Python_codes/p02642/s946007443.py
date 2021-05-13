
from collections import Counter

N = int(input())
X = list(map(int, input().split()))


lim = 10 ** 6 + 10
ok = [True] * (lim + 1)
ans = 0
ctr = Counter(X)
for n in sorted(X):
    if ok[n]:
        if ctr[n] == 1:
            ans += 1
        for j in range(n, lim + 1, n):
            ok[j] = False

print(ans)
