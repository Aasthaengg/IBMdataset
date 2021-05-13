H,W=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(H)]

operations=[]
N=0
for y in range(H):
    for x in range(W):
        if a[y][x]%2==0:
            continue
        else:
            flag=0
            for i,j in ([0,1],[0,-1],[1,0],[-1,0]):
                new_y,new_x=y+i,x+j
                if new_y<0 or new_y>=H or new_x<0 or new_x>=W:
                    continue
                elif a[new_y][new_x]%2!=0:
                    N+=1
                    a[y][x]-=1
                    a[new_y][new_x]+=1
                    operations.append([y+1,x+1,new_y+1,new_x+1])
                    flag=1
                    break
            if flag==0:
                if y!=H-1:
                    N+=1
                    a[y][x]-=1
                    a[y+1][x]+=1
                    operations.append([y+1,x+1,y+2,x+1])
                elif y==H-1 and x!=W-1:
                    N+=1
                    a[y][x]-=1
                    a[y][x+1]+=1
                    operations.append([y+1,x+1,y+1,x+2])

print(N)
for i in range(N):
    print(*operations[i])