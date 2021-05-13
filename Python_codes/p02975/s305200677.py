N=int(input())
*A,=map(int,input().split())
A.sort()

count=A[0]
i=1
while i<N:
    count=count^A[i]
    i+=1

if count==0:
    print('Yes')
else:
    print('No')