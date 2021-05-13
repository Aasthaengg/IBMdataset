H,W=list(map(int,input().split()))
H=H-2
W=W-2

if H < 0:
    H=1
if W < 0:
    W=1

ans=H*W
print(ans)