import numpy as np
H,W = (int(T) for T in input().split())
Map = np.zeros((H+2,W+2),dtype=bool)
for TH in range(0,H):
    Map[TH+1,1:W+1] = [True if T=='#' else False for T in input()] 
Disp = np.full((H,W),'#')
for TH in range(0,H):
    for TW in range(0,W):
        if Map[TH+1,TW+1]==False:
            Disp[TH,TW] = np.sum(Map[TH:TH+3,TW:TW+3])
    print(''.join(Disp[TH,:]))