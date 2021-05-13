import numpy as np
 
L=np.array(list(map(int,input().split())))
ans=0
 
while True:
    if L[0]==L[1] and L[1]==L[2]:
        break
    L=sorted(L-max(L))
    if L[1]<L[2]:
        L[0]+=1
        L[1]+=1
        ans+=1
    else:
        L[0]+=2
        ans+=1

print(ans)