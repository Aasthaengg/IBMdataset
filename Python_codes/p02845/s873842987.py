n=int(input())
A=list(map(int,input().split()))
r,g,b=0,0,0
ans=1
mod=10**9+7
for i in A:
    t=[r,g,b].count(i)
    if t==0:
        print(0)
        exit()
    elif t==1:
        if r==i: r+=1
        elif g==i : g+=1
        else: b+=1
    elif t==2:
        ans*=2  ; ans%=mod
        if r!=i: g+=1
        elif g!=i : b+=1
        else: r+=1
    else:
        ans*=3 ; r+=1 ; ans%=mod

print(ans%mod)