import numpy as np
H,W  = (int(X) for X in input().split())
Grid = np.ones((H+2,W+2),dtype=bool)
for TH in range(0,H):
    Grid[TH+1,1:W+1] = [False if X=='#' else True for X in input()] 

Flag = True
for TH in range(0,H):
    for TW in range(0,W):
        if Grid[TH+1,TW+1]==False:
            Check = np.all([Grid[TH+1,TW],Grid[TH+1,TW+2],Grid[TH,TW+1],Grid[TH+2,TW+1]])
            if Check==True:
                Flag = False
                break
    if Flag==False:
        break
if Flag:
    print('Yes')
else:
    print('No')