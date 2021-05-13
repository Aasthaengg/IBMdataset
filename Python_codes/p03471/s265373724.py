N,Y=map(int,input().split())

for x in range(N+1):
    for y in range(N-x+1):
        z=(Y//1000)-10*x-5*y
        if N==x+y+z:
            print("{} {} {}".format(x,y,z))
            exit()

print("-1 -1 -1")