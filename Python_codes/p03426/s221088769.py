h,w,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

place=[(0,0) for _ in range(h*w+1)]

for r in range(h):
    for c in range(w):
        place[a[r][c]]=(r,c)

dp=[0]*(w*h+1)


for r in range(1,w*h+1):
    if r-d<1:
        continue

    r1,c1=place[r-d]
    r2,c2=place[r]

    dp[r]=dp[r-d]+abs(r1-r2)+abs(c1-c2)

for _ in range(int(input())):
    l,r=map(int,input().split())

    print(dp[r]-dp[l])