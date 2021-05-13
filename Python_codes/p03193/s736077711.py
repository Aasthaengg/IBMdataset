N,H,W=map(int,input().split())
ab=[list(map(int,input().split()))for _ in range(N)]
print(sum((a>=H)*(b>=W)for a,b in ab))