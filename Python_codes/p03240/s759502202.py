n = int(input())
list_XYH1, list_XYH = [ list(map(int,input().split(" "))) for _ in range(n)], []
for x, y, h in list_XYH1:
    if h != 0:
        list_XYH.append([x, y, h])

for i in range(0, 101):
    for j in range(0, 101):
        cnt = 0
        x, y, h = list_XYH[0]
        H = h + abs(i - x) + abs(j - y)
        for x, y, h in list_XYH:
            if h + abs(i - x) + abs(j - y) == H:
                cnt += 1

        if cnt == len(list_XYH) and cnt != 0 and cnt != 1:
            print(i, j, H)
            exit()

list_XYH2 = []
m = pow(10, 10)
for x, y, h in list_XYH1:
    m = min(m, h)
    list_XYH2.append([x, y, h])

for X in range(0, 101):
    for Y in range(0, 101):
        for H in range(m, m + 201):
            cnt = 0
            for x, y, h in list_XYH2:
                if max(H - abs(x - X) - abs(y - Y), 0) == h:
                    cnt += 1

            if cnt == n:
                print(X, Y, H)
                exit()