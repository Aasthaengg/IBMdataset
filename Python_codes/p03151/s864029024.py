N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=sorted([A[i]-B[i]for i in range(N)])
if sum(C)<0:
    print(-1)
else:
    D=[i for i in C if i<0]
    m=sum(D)
    i=0
    while m<0:
        m+=C[N-i-1]
        i+=1
    print(len(D)+i)
