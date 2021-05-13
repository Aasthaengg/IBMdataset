N = int(input())
H = [int(X) for X in input().split()]
Count = 0
while True:
    if len(H)==1:
        Count += H[0]
        break
    else:
        MAXI = H.index(max(H))
        if MAXI==0:
            LR = MAXI+1
        elif MAXI==len(H)-1:
            LR=MAXI-1
        else:
            LR = H.index(max(H[MAXI-1],H[MAXI+1]))
        Count += H[MAXI]-H[LR]
        del H[MAXI]
print(Count)