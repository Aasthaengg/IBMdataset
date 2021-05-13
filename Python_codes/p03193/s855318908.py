N, H, W = map(int, input().split())
ans=0
for i in range(N):
    d, e = map(int, input().split())
    if (d >= H) and (e >= W):
        ans+=1
print(ans)