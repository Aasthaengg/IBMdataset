W,H,n = map(int,input().split())
H_ls = [1] * H
W_ls = [1] * W
for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        for i in range(x):
            W_ls[i] = 0
    elif a == 2:
        for i in range(x,W):
            W_ls[i] = 0
    elif a == 3:
        for i in range(y):
            H_ls[i] = 0
    else:
        for i in range(y,H):
            H_ls[i] = 0
ans = 0
for x in range(W):
    for y in range(H):
        if H_ls[y] and W_ls[x]:
            ans += 1
print(ans)


