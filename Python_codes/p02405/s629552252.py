while(True):
    a=list(map(int,input().split()))
    if(a[0]==0 and a[1]==0):
        break
    for x in range(a[0]):
        if x%2==0:
            for y in range(a[1]):
                if y%2==0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        else:
            for y in range(a[1]):
                if y%2==1:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    print()