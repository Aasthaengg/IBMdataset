
def nmx(x):
    r = 0
    for a in As:
        r += d2[max(0, x-a)]
    return -r
def bsearch(target, min_i, max_i, func):
    # func(index) <= target < func(index+1) となるindexを返す
    if func(max_i) <= target:
        return max_i
    if target < func(min_i):
        return None
    index = (max_i + min_i)//2
    while True:
        if func(index) <= target:
            if target < func(index+1):
                return index
            index, min_i = (index+1 + max_i)//2, index+1
            continue
        index, max_i = (index-1 + min_i)//2, index-1
N, M = map(int, input().split())
As = sorted(list(map(int, input().split())))
mn, mx = As[0], As[-1]

j = 0
n = N
d2 = []
for i in range(mx*2):
    while True:
        if j>=N:
            break
        if i <= As[j]:
            break
        j += 1
        n -= 1
    d2.append(n)
# d2[i] : i以上のaがいくつあるか
# nmx(x) : x以上のペアが何通りあるか
r = bsearch(-M, 1, mx*2, nmx)
r += 1
from itertools import accumulate
aas = list(accumulate([0]+As[::-1]))
rr = 0
c = 0
for a in As[::-1]:
    idx = min(mx*2-1, max(0, r-a))
    rr += a*d2[idx] + aas[d2[idx]]
    c += d2[idx]
rr += (r-1)*(M-c)
print(rr)
