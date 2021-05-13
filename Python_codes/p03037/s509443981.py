n,m=map(int,input().split())
lm,rm=0,10**9
for i in range(m):
    l,r=map(int,input().split())
    lm=max(lm,l)
    rm=min(rm,r)
print(max(0,rm-lm+1))