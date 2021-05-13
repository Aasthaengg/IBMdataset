n,k=map(int,input().split())
A=list(map(int,input().split()))

for i in range(n-k):
    if A[k+i]>A[0+i]:
        print('Yes')
    else:
        print('No')
