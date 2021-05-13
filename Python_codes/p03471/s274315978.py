N,Y=map(int,input().split())

xyz=[]
for x in range(N+1):   
    for y in range(N-x+1):
        z=N-(x+y)
        total=10000*x+5000*y+1000*z
        if total==Y:
            xyz.append([x,y,z])
if xyz:
    print(xyz[0][0],xyz[0][1],xyz[0][2])
else:
    print(-1,-1,-1)