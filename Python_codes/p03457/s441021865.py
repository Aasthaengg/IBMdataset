N = int(input())
txy = [tuple(map(int,input().split())) for _ in range(N)]
t = 0
x = 0
y = 0
for i in range(N):
    nt,nx,ny = txy[i]
    t = nt-t
    x = nx-x
    y = ny-y
    d = abs(x)+abs(y)
    if t < d:
        print("No")
        exit(0)
    elif (t-d)%2 == 1:
        print("No")
        exit(0)
    t,x,y = txy[i]
print("Yes")