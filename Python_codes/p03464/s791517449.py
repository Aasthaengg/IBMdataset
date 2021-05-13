k=int(input())
A=[int(i) for i in input().split()]
mi=2
ma=2

for i in range(k-1,-1,-1):
    mi=((mi+A[i]-1)//A[i])*A[i]
    if mi>ma:
        print(-1)
        break
    ma=(ma//A[i])*A[i]+(A[i]-1)
else:
    if A[-1]==2:
        print(mi,ma)
    else:
        print(-1)
    
