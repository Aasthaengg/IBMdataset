H,N=map(int,input().split())
ab=[list(map(int,input().split()))for _ in range(N)]
ab.sort()

ans=[10**9]*(H+1)
ans[0]=0
i=0
while i<=H:
    for a,b in ab:
        if a+i>H:
            a=H-i
        if ans[i+a]>ans[i]+b:
            ans[i+a]=ans[i]+b
    i+=1

print(ans[H])