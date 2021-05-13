#B問題
N=int(input())
Msum=int(N*(N-1)/2)
subedge=[]
if N%2==0:
    for i in range(int(N/2)):
        subedge.append([i+1,N-i])
    M=Msum-len(subedge)
else:
    for i in range(int((N-1)/2)):
        subedge.append([i+1,N-i-1])
    M=Msum-len(subedge)
print(M)
for i in range(N-1):
    j=0
    for j in range(N-i-1):
        I=i+1
        J=I+j+1
        edge=[I,J]
        if edge not in subedge:
            print(I,J)
        else:
            pass