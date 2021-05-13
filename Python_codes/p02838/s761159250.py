n=int(input())
a=list(map(int,input().split()))

#n=10
#a=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
#a=[3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]

mod=10**9+7
asum=0
for i in range(60):
    zcnt=0
    for ii in range(n):
        asht=a[ii]>>i
        if asht&1==0:
            zcnt+=1
    tmp=(zcnt*(n-zcnt))%mod*((2**i)%mod)
    asum+=(tmp)%mod
               
asum=asum%mod
print(asum)
