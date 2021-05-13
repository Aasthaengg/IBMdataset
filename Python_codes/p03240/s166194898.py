N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]
for x in xyh:
    if x[2] > 0:
        base = x
        break
for i in range(101):
    for j in range(101):
        h = base[2] + abs(i-base[0]) + abs(j-base[1])
        for x in xyh:
            if x[2] != max(h-abs(i-x[0])-abs(j-x[1]),0):
                break
        else:
            print(i,j,h)
            exit()