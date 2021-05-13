H,W = map(int,input().split())
data = [list(input()) for i in range(H)]

A = [[0]*(W) for i in range(H)]
B = [[0]*(W) for i in range(H)]

for i in range(H):
    a = 0
    f = 0
    t = 0
    for j in range(W):
        if data[i][j] == '.' and j < W-1:
            a += 1
            t += 1
        elif data[i][j] == '#':
            for k in range(f,t):
                A[i][k] = a
            t = j+1
            f = j+1
            a = 0
        else:
            for k in range(f,t+1):
                A[i][k] = a+1
for j in range(W):
    b = 0
    f = 0
    t = 0
    for i in range(H):
        if data[i][j] == '.' and i < H-1:
            b += 1
            t += 1
        elif data[i][j] == '#':
            for k in range(f,t):
                B[k][j] = b
            t = i+1
            f = i+1
            b = 0
        else:
            for k in range(f,t+1):
                B[k][j] = b+1
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans,A[i][j]+B[i][j])
print(ans-1)