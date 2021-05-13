n = int(input())
t = [list(map(int,input().split())) for i in range(n)]
for x,y,h in t:
    if h > 0:
        a = [x,y,h]            # hが0でない1つの組(地面以外の部分)

for cx in range(101):
    for cy in range(101):
        flag = True
        ch = abs(a[0]-cx) + abs(a[1] - cy) + a[2]     # 高さ
        for x,y,h in t:
            if h != max(ch - abs(x - cx) - abs(y - cy),0):    # 高さが条件に合うか 
                flag = False
                break
        if flag:
            print(cx,cy,ch)
            exit()