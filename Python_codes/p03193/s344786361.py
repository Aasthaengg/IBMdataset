N, H, W = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for A, B in AB:
    ans += A >= H and B >= W

print(ans)