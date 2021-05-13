n = int(input())
HXY = []
for i in range(n):
    x, y, h = map(int, input().split())
    HXY.append((h, x, y))

HXY.sort(reverse=True)

for i in range(101):
    for j in range(101):
        H = -1
        for k in range(n):
            h, x, y = HXY[k]
            if h > 0:
                temp = h + abs(x-i) + abs(y-j)
                if H > 0:
                    if H != temp:
                        break
                else:
                    H = temp
            else:
                if H - abs(x-i) - abs(y-j) > 0:
                    break
        else:
            if H > 0:
                print(i, j, H)
