N ,H , W = map(int, input().split())
block = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for l in block:
    if (l[0] >= H and l[1] >= W):
        cnt = cnt + 1
print(cnt)