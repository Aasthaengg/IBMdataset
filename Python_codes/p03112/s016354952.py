from bisect import *
A,B,Q=map(int,input().split())
s=[int(input()) for _ in range(A)]
t=[int(input()) for _ in range(B)]
x=[int(input()) for _ in range(Q)]
#print(s,t,x)
for i in x:
    ans=float("inf")
    mins=-float("inf")
    mint=-float("inf")
    maxs=float("inf")
    maxt=float("inf")
    sind=bisect(s,i)
    tind=bisect(t,i)

    if sind!=0:
        mins=s[sind-1]
    if tind!=0:
        mint=t[tind-1]
    if sind!=len(s):
        maxs=s[sind]
    if tind!=len(t):
        maxt=t[tind]
    #print(mins,maxs,mint,maxt)
    slist=[mins,maxs]
    tlist=[mint,maxt]
    ans=min(ans,abs(i-mins)+abs(mins-mint))
    ans=min(ans,abs(i-mins)+abs(mins-maxt))
    ans=min(ans,abs(i-maxs)+abs(maxs-mint))
    ans=min(ans,abs(i-maxs)+abs(maxs-maxt))
    ans=min(ans,abs(i-mint)+abs(mint-mins))
    ans=min(ans,abs(i-mint)+abs(mint-maxs))
    ans=min(ans,abs(i-maxt)+abs(maxt-mins))
    ans=min(ans,abs(i-maxt)+abs(maxt-maxs))
    print(ans)




