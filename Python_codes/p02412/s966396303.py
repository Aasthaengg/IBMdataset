while True:   
    res = 0 
    data = [int(x) for x in input().split()]
    if data == [0,0]:
        break
    for i in range(1,data[0]+1):
        for j in range(i+1,data[0]+1):
            for k in range(j+1,data[0]+1):
                if (i + j + k) == data[1]:
                    res = res + 1
    print(res)
