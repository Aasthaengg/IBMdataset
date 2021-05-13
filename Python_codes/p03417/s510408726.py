l = sorted(list(map(int,input().split())))
#N<=Mとして一般性を失わない
N=l[0]
M=l[1]

if N==M==1:
    print(1)
if N==1 and M>=2:
    print(M-2)
if N==2 and M>=2:
    print(0)
if N>=3 and M>=3:
    print((N-2)*(M-2))