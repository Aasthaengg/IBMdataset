N=int(input())

if N<2 or N%2:
    print(0)
else:
    import math
    ans=0
    n=N//2
    k=int(math.log(n,5))
    for i in range(1,k+1):
        ans+=n//(5**i)
        
    print(ans)