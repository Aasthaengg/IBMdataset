h,w = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(h)]

stack = []

cnt = 0
printlist = [[False]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if l[i][j] % 2 == 1:
            if j < w-1:
                l[i][j+1] += 1
                printlist[i][j] = (i,j+1)
                cnt += 1

for i in range(h):
    if l[i][w-1] % 2 == 1:
        if i < h-1:
            l[i+1][w-1] +=1
            printlist[i][w-1] = (i+1,w-1)
            cnt += 1

print(cnt)
for i in range(h):
    for j in range(w-1):
        if printlist[i][j]:
            x = printlist[i][j]
            print(i+1,j+1,x[0]+1,x[1]+1)
for i in range(h):
    if printlist[i][w-1]:
        x = printlist[i][w-1]
        print(i+1,w,x[0]+1,w)