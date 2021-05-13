N=int(input())
xy=[list(map(int,input().split()))for _ in range(N)]
xy1=[x+y for x,y in xy]
xy2=[-x+y for x,y in xy]
ans1=max(xy1)-min(xy1)
ans2=max(xy2)-min(xy2)
print(max(ans1,ans2))