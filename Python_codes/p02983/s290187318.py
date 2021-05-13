l,r=map(int,input().split())
x=l//2019
if 2019*x<l and r<2019*(x+1):
    ans=float("inf")
    for i in range(l,r):
        for j in range(i+1,r+1):
            ans=min(ans,(i*j)%2019)
    print(ans)
else:
    print(0)