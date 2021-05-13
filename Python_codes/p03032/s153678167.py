N,K=map(int,input().split())
V=list(map(int,input().split()))
ans=0
for a in range(min(N,K)+1):
    for b in range(min(N,K)+1-a):
        v=[]
        value=sum(V[:a])
        v.extend(V[:a])
        if b!=0:
            value=value+sum(V[-b:])
            v.extend(V[-b:])
        v.sort()
        for i in range(min(a+b,K-a-b)):
            if v[i]<0:
                value=value-v[i]
            else:
                break
        ans=max(ans,value)
print(ans)