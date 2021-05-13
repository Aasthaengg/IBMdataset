h, w = map(int,input().split())

field=[]
for _ in range(h):
    field.append(list(input()))

dx=[-1,0,1,-1,1,-1,0,1]
dy=[1,1,1,0,0,-1,-1,-1]

for i in range(h):
    for j in range(w):
        if field[i][j]=="#":
            continue
        count=0
        for x,y in zip(dx,dy):
            if i+x<0 or i+x>h-1 or j+y<0 or j+y>w-1:
                continue
            if field[i+x][j+y]=="#":
                count+=1
        field[i][j] = str(count)

for f in field:
    print(''.join(f))