import math
while True:
    a,b,c=map(float,input().split())
    if a==-1 and b==-1 and c==-1:break
    elif a==-1 or b==-1:
        print("F")
    elif (a+b)>=80:
        print("A")
    elif 80>(a+b) and (a+b)>=65:
        print("B")
    elif 65>(a+b) and (a+b)>=50:
        print("C")
    elif c>=50:print("C")
    elif 50>(a+b) and (a+b)>=30:
        print("D")
    elif 30>(a+b):
        print("F")
