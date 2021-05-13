w,h,n = map(int,input().split())

A = [[0]*w for i in range(h)]

for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                A[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x,w):
                A[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                A[i][j] = 1                
    else:            
        for i in range(y,h):
            for j in range(w):
                A[i][j] = 1                

ans = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == 0:
            ans += 1

print(ans)