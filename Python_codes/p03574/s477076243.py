import numpy as np
from scipy import signal
H, W = list(map(int, input().split()))
com = np.full((1,W),'#')
Mat = np.zeros((H,W))
MAP = np.empty((H,W),int)
mask = [[1,1,1],
        [1,0,1],
        [1,1,1]]
for i in range(H):
    Mat[i] = list(input())==com

MAP = signal.convolve2d(Mat,mask,'same')
outMAP = np.where(Mat,'#',MAP.astype('int'))

for j in outMAP:print(*j,sep='')
# print(MAP)