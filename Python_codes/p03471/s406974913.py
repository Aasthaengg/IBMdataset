N,Y=map(int,input().split())
x,y,z=-1,-1,-1
for i in range(0,Y//10000+1):
    for j in range(0,((Y-i*10000)//5000)+1):
        if (N-i-j>=0)&(10000*i+5000*j+1000*(N-i-j)==Y):
            x=i
            y=j
            z=N-x-y
print(x,y,z)