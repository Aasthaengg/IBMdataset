a,b=map(int,input().split())
G=[[0]*25 for i in range(25)]
x=min(a,b) #地の色
y=max(a,b) #塗る色
C=[x-1,y-x+1]
for i in range(25):
    for j in range(25):
        if C[0]>0:
            G[i][j]=1
            C[0]-=1
        elif C[1]>0:
            G[i][j]=2
            C[1]-=1
        else:
            break
    if C[0]==C[1]==0:
        break

P=[]
if a<b:
    P.append(["....","....","....","...."])
    P.append(["###.","#.#.","###.","...."])
    P.append(["....",".#..","....","...."])
else:
    P.append(["####","####","####","####"])
    P.append(["...#",".#.#","...#","####"])
    P.append(["####","#.##","####","####"])

print(100,100)
for i in range(25):
    for k in range(4):
        s=""
        for j in range(25):
            s+=P[G[i][j]][k]
        print(s)