H,W = map(int,input().split())
T = []
for i in range(H):
    a = list(input())
    T.append(a)

result = [[0]*W for _ in range(H)]
for i in range(H):
    c = 0
    start = 0
    for j in range(W):
        if T[i][j] == "#":
            for k in range(start,j):
                result[i][k] += c
            start = j + 1
            c = 0
        elif j == W-1:
            c += 1
            for k in range(start,j+1):
                result[i][k] += c
        else:
            c += 1

for i in range(W):
    c = 0
    start = 0
    for j in range(H):
        if T[j][i] == "#":
            for k in range(start,j):
                result[k][i] += c
            start = j + 1
            c = 0
        elif j == H-1:
            c += 1
            for k in range(start,j+1):
                result[k][i] += c
        else:
            c += 1

ans = 0
for i in range(H):
    for j in range(W):
        if T[i][j] == ".":
            ans = max(ans,result[i][j]-1)
        else:
            ans = max(ans,result[i][j])
print(ans)