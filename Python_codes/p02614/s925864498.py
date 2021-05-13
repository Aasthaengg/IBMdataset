#ABC 173 C - H and V
import numpy as np

h,w,k = map(int,input().split())
c = np.zeros((h,w)).astype('str')
for i in range(h):
    s = input()
    for j,a in enumerate(s):
        c[i,j] = a
        
cnt = 0
for o in range(2**h):
    for l in range(2**w):
        black = 0
        for m in range(h):
            for n in range(w):
                if ((o>>m)&1==0) and ((l>>n)&1==0) and (c[m,n]=='#'):
                    black += 1
        if black == k:
            cnt += 1
print(cnt)