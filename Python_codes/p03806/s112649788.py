# solution
import io
from scipy.misc import comb

def inpl(): return [int(i) for i in input().split()]

nim,mike,kite = inpl()
inf = float('inf')
H = {(0,0): 0}
for i in range(nim):
    a, b, c = inpl()
    for (ia, ib), ic in H.copy().items():
        H[(ia+a,ib+b)] = min(H.get((ia+a, ib+b), inf),ic+c)

ans = min(H.get((i*mike, i*kite), inf) for i in range(1,401))
print(-1 if ans == inf else ans)    