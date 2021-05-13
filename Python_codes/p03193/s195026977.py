N,H,W = map(int,input().split())
ans = 0
for i in range(N):
    h,w = map(int,input().split())
    if (h >= H)and(w >= W):
        ans += 1

print(ans)



