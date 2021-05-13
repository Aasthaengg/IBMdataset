n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
for Cx in range(101):
    for Cy in range(101):
        flag = False
        check = []
        for x, y, h in info:
            if h == 0:
                continue
            check.append(h+abs(x-Cx)+abs(y-Cy))
        if len(set(check)) == 1:
            flag = True
            ans_h = check[0]
            for x, y, h in info:
                if h != max(ans_h-abs(x-Cx)-abs(y-Cy), 0):
                    flag = False
        if flag:
            print(Cx, Cy, ans_h)
            exit()
