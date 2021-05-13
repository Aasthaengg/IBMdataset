n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

for i in l:
    if i[2] != 0:
        x,y,h = i
# print(x,y,h)

for cx in range(101):
    for cy in range(101):
        h_pre = h+abs(x-cx)+abs(y-cy)
        flag = True
        for i in range(n):
            X,Y,H = l[i]
            if H != max(h_pre-abs(X-cx)-abs(Y-cy),0):
                flag = False
        if flag:
            print(cx,cy,h_pre)
            exit()