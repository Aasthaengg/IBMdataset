import bisect 
from itertools import accumulate

N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
ans = 0

xOK = A[0]*2
xNG = A[-1]*2 + 1
nx = 0
while xOK+1 < xNG:
    x = (xOK + xNG)//2
    nx = 0
    for a in A:
        nx += N-(bisect.bisect_left(A,x-a))
        if nx >= M:
            xOK = x
            break
    else:
        xNG = x

S=[0]+list(accumulate(A))

ans = 0
nnx = 0        
for a in A:
    nx = bisect.bisect_right(A,xOK-a)
    ans += a*(N-nx) + (S[N]-S[nx])
    nnx += (N-nx)
ans += xOK*(M-nnx)
        
    
print(ans)