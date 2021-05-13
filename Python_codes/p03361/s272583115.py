h,w = list(map(int,input().split()))
s = [list(input()) for i in range(h)]

#全部の黒のとこ見て上下左右に黒があればおk！
x = [0,0,1,-1]
y = [1,-1,0,0]

ans = "Yes"
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            flag = False
        else:
            continue
        for k in range(4):
                if 0<=i+x[k]<h and 0<=j+y[k]<w: 
                    if s[i+x[k]][j+y[k]] == "#":
                        flag = True
                    else:
                        continue
        if flag:
            continue
        else:
            print("No")
            exit()


print(ans)


