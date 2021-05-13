X=input()
N=len(X)
cnt=0
sptm=0
ans=0
for i in range(N):
    if X[i]=="S":
        sptm=sptm+1
    if X[i]=="T":
        sptm=sptm-1
    if sptm<0:
        ans=ans+1
        sptm=0
    #print(sptm,ans)
print(ans+max(0,sptm))