N,H = list(map(int, input().split()))
A=0
B=[]
for _ in range(N):
    a,b = list(map(int, input().split()))
    A = max(A, a)
    B.append(b)

B = sorted([b for b in B if b>A], reverse=True)
from itertools import accumulate
B = list(accumulate(B))
total_throw_damage = (B[-1] if len(B)>0 else 0)

HP_after_throw = H - total_throw_damage
if HP_after_throw <= 0:
    for i,b in enumerate(B,1):
        if H<=b:
            print(i)
            exit()
    raise AssertionError('error')
else:
    q,r = divmod(HP_after_throw, A)
    print(len(B)+q+min(1, r))
