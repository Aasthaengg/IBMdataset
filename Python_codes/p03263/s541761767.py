h,w = map(int,input().split())
a = [[] for _ in range(h)]
for i in range(h):
    a[i] = list(map(int,input().split()))
    for j in range(w):
        a[i][j] %= 2
        
z = []
for i in range(h):
    for j in range(w):
        if i%2 == 0:
            k = j
        else:
            k = (w-1)-j
        z.append((i,k))
        
coin = 0
ans = []
for i in range(h*w-1):
    y,x = z[i]
    yy,xx = z[i+1]
    
    if a[y][x] == 1:
        if coin == 0:
            coin = 1
        else:
            coin = 0
            
    if coin == 1:
        ans.append((y+1,x+1,yy+1,xx+1))
        
print(len(ans))
for i in ans:
    print(*i)