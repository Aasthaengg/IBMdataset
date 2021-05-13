W, H, N = map(int, input().split())

a = []
for i in range(N):
    l = list(map(int, input().split()))
    a.append(l)

X = 0 #左から引く領域
Y = 0 #下から引く領域

for j in range(N):
    if a[j][2] == 1: #xより小さい領域を塗りつぶす
        if a[j][0] > X:
            X = a[j][0]
        else:
            pass
    elif a[j][2] == 2: #xより大きい領域を塗りつぶす
        if a[j][0] < W:
            W = a[j][0]
        else:
            pass
    elif a[j][2] == 3: #yより小さい領域を塗りつぶす
        if a[j][1] > Y:
            Y = a[j][1]
        else:
            pass
    elif a[j][2] == 4: #yより大きい領域を塗りつぶす
        if a[j][1] < H:
            H = a[j][1]
        else:
            pass
    else:
        print('Error')

W = W - X
H = H - Y

if W <= 0:
    W = 0
else:
    pass

if H <= 0:
    H = 0
else:
    pass

ans = W * H
if ans <= 0:
    print(0)
else:
    print(ans)