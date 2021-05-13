datalist = {}
Flag = True
for i in range(10000):
    if Flag:
        n = int(input())
        if n == 0:
            Flag = False
        else:
            datalist[i+1] = n
#print(datalist)
for i in range(1, len(datalist)+1):
    print("Case {}: {}".format(i, datalist[i]))

