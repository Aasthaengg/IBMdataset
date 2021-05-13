from collections import deque

N=int(input())
d=deque()
S=list(map(int,input().split()))

revflag=False

for i in range(N):
    if revflag==False:
        d.append(S[i])
        revflag=True
    else:
        d.appendleft(S[i])
        revflag=False
    
if revflag==True:
    d.reverse()

Z=list(d)
Z=[str(a) for a in Z]
Z=" ".join(Z)
print(Z)
