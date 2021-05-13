N,H,W=map(int,input().split())
cnt=0
for i in range(N):
    h,w=map(int,input().split())
    if h>=H and w>=W:
        cnt+=1
print(cnt)