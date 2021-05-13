while True:
    i,j=list(map(int,input().split()))
    if i==0 and j==0:
        break
    for y in range(i):
        for x in range(j):
            print("#",end="")
        print("")
    print("")

