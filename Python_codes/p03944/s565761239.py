# 63 B - すぬけ君の塗り絵 2 イージー
W,H,N = map(int,input().split())

X = []
Y = []
A = []
for _ in range(N):
    x,y,a = map(int,input().split())
    x -= 1;y -= 1
    X.append(x)
    Y.append(y)
    A.append(a)

mtrx = [['.']*W for _ in range(H)]

for a,(x,y) in zip(A,zip(X,Y)):
    if a == 1:
        for i in range(H):
            for j in range(x+1):
                mtrx[i][j] = '#'
    if a == 2:
        for i in range(H):
            for j in range(x+1,W):
                mtrx[i][j] = '#'
    if a == 3:
        for i in range(y+1):
            mtrx[i] = ['#']*W
    if a == 4:
        for i in range(y+1,H):
            mtrx[i] = ['#']*W

ans = 0
for i in range(H):
    for j in range(W):
        if mtrx[i][j] == '.':
            ans += 1
print(ans)