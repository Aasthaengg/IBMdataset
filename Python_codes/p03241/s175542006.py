N,M = map(int,input().split())
if M==1: print(1);exit()
if N==1: print(M); exit()
ans = 1
for i in range(2,int(M**(1/2)+2)):
    if M%i==0:
        p = M//i
        if p <=M/N:
            ans = max(p,ans) 
        if i<=M/N:
            ans = max(ans,i)
print(ans)