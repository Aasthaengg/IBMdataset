def Lucas_Update(L0,L1):
    L2=L0+L1
    return L2
N=int(input())
L=[2,1]
if N==0:
    print(2)
elif N==1:
    print(1)
else:
    for i in range(2,N+1):
        L.append(Lucas_Update(L[i-1],L[i-2]))
    print(L[N])