while True:
    num = list(map(int,input().split()))
    if(num[0] == 0 and num[1] == 0):break
    else:
        for i in range(num[0]):
            for j in range(num[1]):
                print("#",end="")
            print("")
        print("")

