while True:
    num = list(map(int,input().split()))
    if(num[0] == 0 and num[1] == 0): break
    else:
        flag = False
        for i in range(num[0]):
            str = ""
            if(i == 0 or i == num[0]-1): flag=True
            else: flag=False
            for j in range(num[1]):
                if(j == 0 or j == num[1]-1 or flag):
                    str = str + "#"
                else:
                    str = str + "."
            print(str)
        print()
                    
