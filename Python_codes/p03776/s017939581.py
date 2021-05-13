
from collections import Counter

N, A, B = map(int, input().split())

v = list(map(int, input().split()))
v.sort(reverse=True)

ave_max = sum(v[:A]) / A

counter = Counter(v)
cnt = counter[v[0]]
#最大のｖが一つだけなら残りの選び方、複数あるならその選び方も考慮
ans = 0
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]
if cnt < A:
    m = v[A-1]
    n = counter[m] # 最小値の個数
    r = v[:A].count(m)
    ans = cmb(n,r)
elif cnt == A:
    ans = 1
    
else:
    for i in range(A, min(cnt, B) + 1):

        ans += cmb(cnt, i)

print(ave_max)
print(ans)