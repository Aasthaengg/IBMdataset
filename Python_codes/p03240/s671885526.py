n = int(input())
XYH = []
for i in range(n):
    x, y, h = map(int, input().split())
    XYH.append((h, x, y))

XYH.sort(reverse=True)


for i in range(101):
    for j in range(101):
        H = -1
        flag = True
        for k in range(n):
            h, x, y = XYH[k]
            if H == -1:
                H = abs(x-i)+abs(y-j)+h
            else:
                if max(H-abs(x-i)-abs(y-j), 0) != h:
                    flag = False
        if flag:
            print(i, j, H)
            exit()
