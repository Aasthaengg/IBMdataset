W,H,X,Y = map(int,input().split())
xwari = min(X*H,(W-X)*H)
ywari = min(Y*W,(H-Y)*W)
if W/2 == X and H/2 == Y:
    f = 1
else:
    f = 0
print(W*H/2, f)
