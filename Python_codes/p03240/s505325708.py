n = int(input())
XYH = [list(map(int, input().split())) for _ in range(n)]

for i in range(101):
    for j in range(101):
        temp = -1
        for x, y, h in XYH:
            if h == 0:
                continue
            temp = h + abs(x - i) + abs(y - j)
            break
        flag = 0
        for x, y, h in XYH:
            kouho = temp - (abs(x - i) + abs(y - j)) - h
            if kouho == 0:
                continue
            elif h == 0 and kouho < 0:
                continue
            else:
                flag = 1
                break
        if not flag:
            print(i, j, temp)
            exit()

