h,w,d=map(int,input().split())
ind={}
for i in range(h):
    l=list(map(int,input().split()))

    for j in range(w):
        ind[l[j]]=(i,j)
dp=[0]*(h*w)
for i in range(d+1,h*w+1):
    x,y=ind[i]
    z,q=ind[i-d]
    dp[i-1]=abs(z-x)+abs(y-q)+dp[i-d-1]


q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(dp[r-1]-dp[l-1])