W, H, N = map(int,input().split())

X = [True]*W
Y = [True]*H

for i in range(N):
    x, y, a = map(int,input().split())
    if a == 1:
        for j in range(x):
            X[j] = False
    if a == 2:
        for j in range(x,W):
            X[j] = False
    if a == 3:
        for j in range(y):
            Y[j] = False
    if a == 4:
        for j in range(y,H):
            Y[j] = False

ans = 0
for i in range(W):
    for j in range(H):
        if X[i] and Y[j]:
            ans += 1
            
print(ans)