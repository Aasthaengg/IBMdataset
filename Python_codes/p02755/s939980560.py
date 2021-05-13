import math
A,B=map(int,input().split())
amin = A/0.08
amax = (A+1)/0.08
bmin = B/0.1
bmax = (B+1)/0.1

if bmin == amax or amin == bmax:
    print(-1)
else:
    ans = max(amin, bmin)
    ans = math.ceil(ans)
    if ans < amax and ans < bmax:
        print(ans)
    else:
        print(-1)
