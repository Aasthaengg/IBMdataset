h,w = map(int,input().split())

arr = ["0" *(w + 2)]
for i in range(h):
    arr.append("0" + input() + "0")
arr.append("0" *(w + 2))

flg = [[-1 for i in range(w+2)] for j in range(h+2)]

ima = []
for i in range(h+2):
    for j in range(w+2):
        if arr[i][j] == "#":
            ima.append([i,j])
            flg[i][j] = 0

while len(ima) > 0:
    tugi = []
    for x,y in ima:
        if arr[x+1][y] == "." and flg[x+1][y] == -1:
            tugi.append([x+1,y])         
            flg[x+1][y] = flg[x][y] + 1
        if arr[x-1][y] == "." and flg[x-1][y] == -1:
            tugi.append([x-1,y])
            flg[x-1][y] = flg[x][y] + 1
        if arr[x][y+1] == "." and flg[x][y+1] == -1:
            tugi.append([x,y+1])
            flg[x][y+1] = flg[x][y] + 1
        if arr[x][y-1] == "." and flg[x][y-1] == -1:
            tugi.append([x,y-1])
            flg[x][y-1] = flg[x][y] + 1
    ima = tugi

ans = -1
for i in flg:
    for j in i:
        if ans < j:
            ans = j
print(ans)