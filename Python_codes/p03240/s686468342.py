N = int(input())
xyh = [list(map(int, input().split())) for _ in range(N)]
xyh = sorted(xyh, key=lambda x:x[2])
ans = []
for i in range(101):
    for j in range(101):
        pre = xyh[-1][2] + abs(i-xyh[-1][0]) + abs(j-xyh[-1][1])
        valid = True
        for k in range(N):
            x, y, h = xyh[k]
            a = abs(x-i) + abs(y-j)
            if max(pre-a, 0) != h:
                valid = False

        if valid and pre >= 1:
            print(i, j, pre)
            exit()