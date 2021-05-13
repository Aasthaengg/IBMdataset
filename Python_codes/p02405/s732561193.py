while True:
    num = list(map(int,input().split()))
    if(num[0] == 0 and num[0] == 0): break
    else:
        flag = False
        for i in range(num[0]):
            str = ""
            if(i % 2 == 0):flag = True
            else: flag = False
            for j in range(num[1]):
                if(flag):
                    str = str + "#" 
                    flag = False
                else:
                    str = str + "."
                    flag = True
            print(str)
        print("")
