
import numpy as np
import sys
sys.setrecursionlimit(100000)


def acinput():
    return list(map(int, input().split(" ")))



H, W = acinput()

# d=[0]*26
d = {}

for i in range(H):

    tmp = list(input())
    for c in tmp:
        try:
            d[c] += 1
        except:
            d[c] = 1
mod2 = mod4 = 0

mod1=0
for k in d:
    if d[k] % 4 == 0:
        mod4 += 1
    elif d[k] % 2 == 0:
        mod2 += 1
    elif d[k]%2==1:
        mod1+=1


am=H%2
bm=W%2

A1=0

if am==0 and bm==0:
    resid4 = np.floor((H)*(W))-mod4
    A2=0
elif am==0 and bm==1:
    resid2 = np.floor(W-1)-mod2
    resid4 = np.floor((H-1)*(W))-mod4
    A2=H//2
elif am==1 and bm==0:
    resid2 = np.floor(W-1)-mod2    
    resid4=np.floor((H-1)*(W))-mod4
    A2=W//2
else:
    resid2 = np.floor(W-1)+H-1-mod2
    resid4 = np.floor((H-1)*(W-1))-mod4
    A2=(W+H-2)//2
    A1=1

#print(resid4,mod2)

res = False

#print(A2,mod2)
if A2>=mod2 and A1>=mod1:
    res=True

if res:
    print("Yes")
else:
    print("No")