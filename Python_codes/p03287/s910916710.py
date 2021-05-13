n, m = map(int, input().split())
A = list(map(int, input().split()))
from itertools import accumulate
B = [0]+A
B = list(accumulate(B))
d = {}
ans = 0
for i in range(n+1):
    s = B[i]%m
    if s in d:
        ans += d[s]
        d[s] += 1
    else:
        d[s] = 1
print(ans)
