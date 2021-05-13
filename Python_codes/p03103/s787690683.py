N,M=map(int,input().split())
l=sorted(list(tuple(map(int,input().split()))for i in range(N)),key=lambda x:x[0])
c=0
ans=0
for v,k in l:
    ans+=min(k,M-c)*v
    c+=min(k,M-c)
    if c==M:
        print(ans);exit()
