n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
tt=[float("inf") for i in range(n)]
ans=[False for i in range(n)]
tmp=0
mod=10**9+7
for i in range(n):
    if t[i]>tmp:
        
        tt[i]=t[i]
        ans[i]=True
        tmp=t[i]
    else:
        tt[i]=tmp
tmp=0
for i in range(n-1,-1,-1):
    if ans[i]==True and a[i]<t[i]:
        print(0)
        exit()
    if a[i]>tmp:
        if ans[i]==True and a[i]!=t[i]:
            print(0)
            exit()
        tt[i]=a[i]
        ans[i]=True
        tmp=a[i]
    else:
        if ans[i]==False and tmp<tt[i]:
            tt[i]=tmp    
tmp=1
for i in range(n):
    if ans[i]==False:
        tmp*=tt[i]
        tmp%=mod
print(tmp%mod)