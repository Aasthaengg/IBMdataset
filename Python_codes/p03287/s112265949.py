n, m = map(int, input().split())
a = list(map(int , input().split()))

class Cumulative_Sum:
    def __init__(self, a):
        la = len(a)
        self.s = [0] * (la + 1)
        for i in range(la):
            self.s[i+1] = self.s[i] + a[i]
    # s[l]からs[r]までの和
    def sum(self, l, r):
        return self.s[r] - self.s[l]

cs = Cumulative_Sum(a)
from collections import defaultdict
b = defaultdict(int)

for i in range(n+1):
    b[cs.s[i] % m] += 1

ans = 0
for bi in b:
    if b[bi] > 1:
        ans += b[bi] * (b[bi] - 1) // 2
print(ans)

"""
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if cs.sum(i, j) % m == 0:
            ans += 1
#print(ans)
"""