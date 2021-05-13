N, H, W = map(int, input().split())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    ans += (A >= H and B >= W)
print(ans)
