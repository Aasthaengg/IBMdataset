"""
1~Nまでを素因数分解して、素因数の数を足し合わせればよい。
計算量としては、O(N*√N)
"""
from collections import Counter
N = int(input())
count = Counter([])
for i in range(1,N+1):
    tmp = []
    d = 2
    while d**2 <= i:
        if i%d == 0:
            i //= d
            tmp.append(d)
        else:
            d += 1
    if i != 1:
        tmp.append(i)
    count += Counter(tmp)

mod = 10**9 +7
ans = 1
for v in count.values():
    ans *= (v+1)
ans %= mod
print(ans)