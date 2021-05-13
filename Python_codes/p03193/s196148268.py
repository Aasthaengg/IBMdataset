N,H,W = list(map(int, input().split()))

ans = 0
for i in range(N):
    A,B = list(map(int, input().split()))
    if A >= H and B >= W:
        ans += 1
print(ans)