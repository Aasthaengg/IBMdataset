import math
def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
from collections import Counter
N,M = map(int,input().split())
a_ls = list(map(int, input().split()))

for i in range(N):
    a_ls[i] = a_ls[i]%M
a_csum = [0] * N
now = 0
for i in range(N):
    now += a_ls[i]
    now %= M
    a_csum[i] = now

a_csum.append(0)
c = Counter(a_csum)
ans = 0
for value,time in c.items():
    if time >= 2:
        ans += nCr(time,2)
print(ans)