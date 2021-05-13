N,M=map(int,input().split())

x=[-1]*N
ok=True
for _ in range(M):
    s,c=map(int,input().split())
    s-=1
    if (s==0 and c==0 and N>1) or x[s]!=-1 and x[s]!=c:
        ok=False
        break
    x[s]=c

if ok:
    ans=0
    for i in range(N):
        if x[i]==-1:
            x[i]=0 if (i>0 or N==1) else 1
        ans=ans*10+x[i]
    print(ans)
else:
    print(-1)
