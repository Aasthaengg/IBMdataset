N = int(input())
LR = [[int(x) for x in input().split()] for _ in range(N)]

cnt = 0
for l, r in LR:
    cnt += r - l + 1
print(cnt)