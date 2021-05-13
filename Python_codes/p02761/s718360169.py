N,M=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(M)]

D=[-1]*N
ans=True

for s,c in S:
    if D[s-1] == -1:
        D[s-1]=c
    else:
        if D[s-1] != c:
            ans=False

if D[0]==0 and 1<N: ans=False
if D[0]==-1:
    if N==1:
        D[0]=0
    else:
        D[0]=1

for i in range(N):
    if D[i]==-1: D[i]=0 
     
print(''.join(map(str,D)) if ans else -1)