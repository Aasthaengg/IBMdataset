N,Y = map(int,input().split())

for x in range(N+1):
    for y in range(N+1-x):
        p = x*10000 + y*5000
        if p > Y: break
        rem = Y - p
        z = rem//1000
        if x+y+z == N:
            print(x,y,z)
            exit()
print(-1,-1,-1)