import sys
def input():
    return sys.stdin.readline()[:-1]
a,b=map(int,input().split())
grid=[[0]*100 for i in range(100)]
grid[0]
for i in range(50):
    for j in range(100):
        grid[50+i][j]=1
h,i,j=99,0,0

while(i<a-1):
    grid[h][j]=0
    i+=1
    j+=2
    if j==100:
        j=0
        h-=2

h,i,j=0,0,0
while(i<b-1):
    grid[h][j]=1
    i+=1
    j+=2
    if j==100:
        j=0
        h+=2
print("100 100")
for i in range(100):
    tmp=""
    for j in range(100):
        if grid[i][j]==1:
            tmp+="#"
        else:
            tmp+="."
    print(tmp)