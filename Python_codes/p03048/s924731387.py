R,G,B,N=map(int,input().split())
ans=0
naxR=N//R
naxG=N//G
for r in range(naxR+1):
    for g in range(naxG+1):
        if (N-r*R-g*G)/B>=0 and (N-r*R-g*G)%B==0:
            ans+=1
print(ans)