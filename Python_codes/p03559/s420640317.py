N=int(input())
A,B,C=[sorted(map(int,input().split())) for i in range(3)]
i,j=0,0
r=0
for b in B:
    while i<N and A[i]<b:
        i+=1
    while j<N and C[j]<=b:
        j+=1
    r+=i*(N-j)
print(r)