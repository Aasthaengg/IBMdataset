# coding: utf-8
# Here your code !

def func():
    try:
        line=input().rstrip()
        list=line.split(" ")
        a=int(list[0])
        b=int(list[1])
        c=int(list[2])
    except:
        print("input error")
        return -1
    
    if((a<b) and (b<c)):
        print("Yes")
    else:
        print("No")

func()