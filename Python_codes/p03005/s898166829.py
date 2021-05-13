a= list(map(int,input().split()))
N=a[0]
K=a[1]

if K==1:
    print(0)
else:
    print(N-K)
