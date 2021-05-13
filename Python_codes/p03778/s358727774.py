W,a,b=map(int,input().split())
if a<=b<=a+W or b<=a<=b+W:
    print(0)
else:
    A=[a,a+W]
    B=[b,b+W]
    ans=10**9
    for u in A:
        for v in B:
            ans=min(abs(u-v),ans)
    print(ans)