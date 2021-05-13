h,w,a,b = map(int,input().split())
ans = [[0]*w for i in range(h)]

for i in range(h):
    if i >= h-b:
        for j in range(w-a,w):
            ans[i][j] = 1
    else:
        for j in range(w-a):
            ans[i][j] = 1
for i in ans:
    print(*i,sep="")