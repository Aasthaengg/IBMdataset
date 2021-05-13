N=int(input())
dx,dy,dt=0,0,0
count=0
for i in range(N):
    t,x,y=map(int,input().split())
    if (x+y+t)%2 == 0 and abs(x-dx) + abs(y-dy) <= abs(t-dt):
        count+=1
    dx,dy,dt=x,y,t

if count==N:
    print("Yes")
else:
    print("No")


