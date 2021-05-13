from collections import deque
h,w = map(int,input().split())
map_input = [list(input()) for i in range(h)]

score = [[10**10]*(w+1) for i in range(h+1)]
score[0][1] = 0
score[1][0] = 0

for i in range(h):
    for j in range(w):
        tmp1 = score[i][j+1] + (map_input[i][j]=='#' and (i==0 or map_input[i-1][j]=='.'))
        tmp2 = score[i+1][j] + (map_input[i][j]=='#' and (j==0 or map_input[i][j-1]=='.'))
        score[i+1][j+1]=min(tmp1,tmp2)
print(score[-1][-1])