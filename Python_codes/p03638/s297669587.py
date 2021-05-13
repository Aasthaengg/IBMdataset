h,w = map(int,input().split())
n = int(input())
l = list(map(int,input().split()))
ans = [[0]*w for i in range(h)]
x,y = 0,0
z = 1
num = 1
for i in range(n):
    count = 0
    while count < l[i]:
        ans[x][y] = i+1
        count += 1
        if z == 1:
            if y == w-1:
                x += 1
                z = 2
                
            else:
                y += 1
        elif z == -1:
            if y == 0:
                x += 1
                z = 2
            else:
                y -= 1
        elif z == 2:
            if w != 1:
                if y == 0:
                    y += 1
                    z = 1
                else:
                    y -= 1
                    z = -1
            else:
                x += 1
        
for i in ans:
    print(*i)
                

