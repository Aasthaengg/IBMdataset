import math
while True :
    alist = [ x for x in input().split() ]
    if alist[1] == "?" :
        break
    elif alist[1] == "*" :
        print(int(alist[0]) * int(alist[2]))
    elif alist[1] == "/" :
        print(math.floor(int(alist[0]) / int(alist[2])))
    elif alist[1] == "+" :
        print(int(alist[0]) + int(alist[2]))
    elif alist[1] == "-" :
        print(int(alist[0]) - int(alist[2]))