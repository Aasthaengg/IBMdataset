n = int(input())
info = []
for i in range(n):
    x,y,h = map(int,input().split())
    info.append((x,y,h))
info.sort(key=lambda x:x[2], reverse=True)

for i in range(0,101):
    for j in range(0,101):
        crt_h = info[0][2] + abs(info[0][0]-i) + abs(info[0][1]-j)
        flag = True
        for k in range(1, n):
            tar_x = info[k][0]
            tar_y = info[k][1]
            tar_h = info[k][2]
            H = tar_h + abs(tar_x - i) + abs(tar_y - j)
            if tar_h != 0:
                if H != crt_h:
                    flag = False
            else:
                if crt_h > H:
                    flag = False
        if flag:
            print(i,j,crt_h)




