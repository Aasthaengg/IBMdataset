N=int(input())
*A,=map(int,input().split())

B=[0]*N
i=0
while i<N:
    B[i]=A[i]%2
    i+=1

if B.count(1)%2==1 and 2<=N:
    print('NO')

else:
    print('YES')