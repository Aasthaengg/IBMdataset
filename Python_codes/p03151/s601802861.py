n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
import numpy as np
A=np.array(A)
B=np.array(B)

if np.sum(A)<np.sum(B):
    print(-1)
    exit()

difAB=A-B
negdif=difAB[difAB<0]
posdif=sorted(difAB[difAB>0], reverse=True)
ans=len(negdif)
needs=sum(negdif)
i=0
while needs<0:
    needs+=posdif[i]
    ans+=1
    i+=1

print(ans)