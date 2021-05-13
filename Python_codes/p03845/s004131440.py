n=int(input())
t=list(map(int,input().split()))
m=int(input())
px=[list(map(int,input().split())) for i in range(m)]
time=sum(t)
for i in range(m):
    print(time-t[px[i][0]-1]+px[i][1])