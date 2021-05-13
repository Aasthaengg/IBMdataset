import numpy as np
N,H,W = map(int,input().split())
ab=[]
for i in range(N):
    ab.append(list(map(int,input().split())))
ab=np.array(ab)
print(ab[(ab[:,0]>=H)&(ab[:,1]>=W)].shape[0])