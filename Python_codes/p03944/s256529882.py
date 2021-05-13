w,h,n = map(int,input().split())
cnt = 0
k = [[False for i in range(w)] for j in range(h)]
while(cnt < n):
    x,y,a = map(int,input().split())
    
    if(a == 1):
        for i in range(h):
            for j in range(x):
                k[i][j] = True
    elif(a == 2):
        for i in range(h):
            for j in range(x,w):
                k[i][j] = True
    elif(a == 3):
        for i in range(y):
            for j in range(w):
                k[i][j] = True
    elif(a == 4):
        for i in range(y,h):
            for j in range(w):
                k[i][j] = True
    cnt += 1
sum = 0
for i in range(h):
    sum += k[i].count(False)
print(sum)