N,A,B = map(int, input().split())
V = [int(v) for v in input().split()]

V.sort(reverse=True)
s = 0
for i in range(A):
    s += V[i]
    idx = i
    
av = s/A
for i in range(A, B):
    if V[i] < av:
        break
    s += V[i]
    av = s/(i+1)
    idx = i
    
cnt_up = 0
cnt_same = 0
for i in range(N):
    if V[i] > V[idx]:
        cnt_up += 1
    elif V[i] == V[idx]:
        cnt_same += 1
        
print(av)

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


if cnt_up > 0:
    ans = cmb(cnt_same, A-cnt_up)
else:
    ans = 0
    for i in range(A, B+1):
        if cnt_same < i:
            break
        ans += cmb(cnt_same, i)
        
print(ans)