from collections import deque

H,W = map(int, input().split())
Ss = [str(input()) for _ in range(H)]

yoko = [[0 for _ in range(W)] for _ in range(H)]
tate = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Ss[i][j] == "#" or yoko[i][j] != 0:
            continue
        else:
            paths = [[i,j]]
            temp = 1
            for k in range(j+1, W):
                if Ss[i][k] == ".":
                    temp+=1
                    paths.append([i,k])
                else:
                    break
            for path in paths:
                yoko[path[0]][path[1]] = temp

for i in range(H):
    for j in range(W):
        if Ss[i][j] == "#" or tate[i][j] != 0:
            continue
        else:
            paths = [[i,j]]
            temp = 1
            for k in range(i+1, H):
                if Ss[k][j] == ".":
                    temp+=1
                    paths.append([k,j])
                else:
                    break
            for path in paths:
                tate[path[0]][path[1]] = temp

answer = 0
for i in range(H):
    for j in range(W):
        if answer < tate[i][j]+yoko[i][j]-1:
            answer = tate[i][j]+yoko[i][j]-1
print(answer)