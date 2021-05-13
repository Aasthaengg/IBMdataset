N, H, W = map(int, input().split())
cnt = 0
for i in range(N):
    A, B = map(int, input().split())
    if(A >= H and B >= W):
        cnt += 1
print(cnt)