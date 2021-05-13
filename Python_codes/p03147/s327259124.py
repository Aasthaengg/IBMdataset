n=int(input())
h=list(map(int,input().split()))
hm=max(h)

ans=0
for i in range(hm,0,-1):
    t=1
    for j in range(n):
        if h[j]>=i:
            ans+=t
            t=0
        else:
            t=1

print(ans)
