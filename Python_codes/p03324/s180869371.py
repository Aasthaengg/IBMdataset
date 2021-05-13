D,N=map(int,input().split())

B=100**D
I=0
A=0
while I<N:
    A+=B
    if (A//B)%100:
        I+=1
print(A)
