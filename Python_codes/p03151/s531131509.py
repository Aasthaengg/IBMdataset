n = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
from itertools import accumulate
cs = [a-b for a,b in zip(As,Bs)]
cs.sort(reverse=True)
#負の数を埋めるのに、正の数を何個使うか
p = [0]+[c for c in cs if c > 0]
m = [c for c in cs if c < 0]


ans = 0

m_all = sum(m)
acc = list(accumulate(p))
ans += len(m)
for i,p in enumerate(acc):
    if p >= -m_all:
        break
ans += i


if sum(As) < sum(Bs):
    print(-1)
else:
    print(ans)