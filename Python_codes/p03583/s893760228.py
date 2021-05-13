n=int(input())

for x in range(1,3501):
    for y in range(1,3501):
        if (4*x*y-n*y-n*x)>0 and (n*x*y)%(4*x*y-n*y-n*x)==0:
            z=(n*x*y)//(4*x*y-n*y-n*x)
            print(x,y,z)
            exit()
