n = int(input())

xyh = [list(map(int, input().split())) for _ in range(n)]

xyh.sort(key=lambda x:x[2], reverse=True)

for i in range(101):
    meta = False
    for j in range(101):
        H = 0
        flag = True
        for x, y, h in xyh:
            #print(x, y, h, H)
            if H == 0:
                H = abs(x - i) + abs(y - j) + h
            elif max(H - abs(x - i) - abs(y - j), 0) != h:
                flag = False
                break
        if flag:
            print(i, j, H)
            meta = True
            break
    if meta:
        break
