from collections import deque

h,w = map(int,input().split())
matrix = [["a" for _ in range(w+2)]] + [list("a" + input() + "a") for _ in range(h)] + [["a" for _ in range(w+2)]]

matrix_list1 = deque()
cnt = 0

#黒いタイルの位置情報を確認
for i in range(1,h+1):
    for j in range(1,w+1):
        if matrix[i][j] == "#":
            matrix_list1.append([i,j])

#白いタイルが無くなるまで、黒いタイルを増やす
while len(matrix_list1) != 0:     
    for _ in range(len(matrix_list1)):
        x,y = matrix_list1.popleft()
        if matrix[x+1][y] == ".":
            matrix[x+1][y] = "#"
            matrix_list1.append([x+1,y])
        if matrix[x-1][y] == ".":
            matrix[x-1][y] = "#"
            matrix_list1.append([x-1,y])
        if matrix[x][y+1] == ".":
            matrix[x][y+1] = "#"
            matrix_list1.append([x,y+1])
        if matrix[x][y-1] == ".":
            matrix[x][y-1] = "#"
            matrix_list1.append([x,y-1])
    else:
        if len(matrix_list1) > 0:
            cnt += 1
    
print(cnt)