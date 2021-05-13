# coding: utf-8
# Your code here!

n,k=map(int,input().split())
v=list(map(int,input().split()))
ans=0

for a in range(n+1):
    for b in range(n+1):
        if a+b>n:
            break
        if a+b>k:
            break
        if a+b==n:
            val=sum(v)
            ans=max(ans,val)
            # print(a,b,val)
            continue
        tmp=v[:a]+v[::-1][:b]
        val=sum(tmp)
        c=k-a-b
        tmp.sort()
        for i in range(min(c,a+b)):
            if tmp[i]<0:
                val-=tmp[i]
            else:
                break
        ans=max(ans,val)
        # print(a,b,val)
print(ans)
