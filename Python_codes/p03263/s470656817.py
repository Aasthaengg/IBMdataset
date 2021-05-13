h,w = map(int,input().split())
A = []
for i in range(h):
    A.append(list(map(int,input().split())))
visit = [[0]*w for i in range(h)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
cnt=0
yx = []
for i in range(h):
    for j in range(w):
        visit[i][j]=1
        if A[i][j] %2==1:
            for dy,dx in d:
                if 0<=i+dy<h and 0<=j+dx<w:
                    if visit[i+dy][j+dx] ==0:
                        A[i][j] -=1
                        A[i+dy][j+dx] +=1
                        cnt+=1
                        yx.append((i+1,j+1,i+dy+1,j+dx+1))
                        break
print(cnt)
for i in range(cnt):
    print(*yx[i])
