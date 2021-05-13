# cook your dish here
n=int(input())
v=list(map(int,input().split()))
if 1 not in v:
    print(-1)
else:
    ans=0
    num=1
    for i,e in enumerate(v):
        if e==num:
            num+=1
            ans+=1
            
            
    print(n-ans)
