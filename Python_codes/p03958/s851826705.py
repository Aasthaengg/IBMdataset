K,T=map(int,input().split())
a=list(map(int,input().split()))
M=max(a)
sm=sum(a)
if (2*M)<=sm:
    print(0)
else:
    ans=2*M-sm
    print(ans-1)