a,b=map(int,input().split())

grid=[["#"for i in range(100)]for j in range(50)]+[["."for i in range(100)]for j in range(50)]
#print(grid)

print(100,100)
a-=1  #下半分がその色だから
for i in range(1,49):
    for j in range(1,99):
        if all([ grid[i+x][j+y]=="#" for x,y in ((0,0),(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))]):
            if a==0:
                break
            grid[i][j]="."
            a-=1

            
    if a==0:
        break
b-=1
for i in range(51,99):
    for j in range(1,99):
        if all([ grid[i+x][j+y]=="." for x,y in ((0,0),(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))]):
            if b==0:
                break
            grid[i][j]="#"
            b-=1

            
    if b==0:
        break
for i in grid:
    print("".join(i))