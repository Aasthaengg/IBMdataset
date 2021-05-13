import math
a,b=map(int,input().split())

ans = abs(a-b)
M = max(a,b)

if ans%2==0:
    ans//=2
    print(M-ans)
else:
    print("IMPOSSIBLE")