import sys

N,M=map(int,input().split())

x=[-1]*N
valid=True
for _ in range(M):
    s,c=map(int,input().split())
    if x[s-1]!=-1 and x[s-1]!=c:
        print(-1)
        sys.exit()
    x[s-1]=c

if N>1 and x[0]==0:
    print(-1)
else:
    ans=0
    for i in range(N):
        if x[i]==-1:
            if i>0 or N==1:
                x[i]=0
            else:
                x[i]=1
        ans=ans*10+x[i]
    print(ans)
