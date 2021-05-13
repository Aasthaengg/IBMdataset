N, H, W = (int(i) for i in input().split())
set = [[int(i) for i in input().split()] for i in range(N)]
cnt = 0
for i in range(N):
    cnt += 1 if set[i][0]>=H and set[i][1]>=W else 0
print(cnt)