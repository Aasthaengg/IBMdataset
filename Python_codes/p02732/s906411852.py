import collections
import math

n = int(input())
a = [int(i) for i in input().split()]

def com(n, r):
    if n > 1:
        ann = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    else:
        ann = 0
    return ann

b = collections.Counter(a)
ans = []
for i in b:
    ans.append(com(b[i],2))
anss = sum(ans)

for i in range(n):
    t = b[a[i]]
    print(anss - (t-1))