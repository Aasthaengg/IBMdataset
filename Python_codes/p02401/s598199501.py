import math
while True:
    x = input().split()
    a = int(x[0])
    b = int(x[2])
    oprnd = x[1]
    if oprnd=="+":
        print(a+b)
    elif oprnd=="-":
        print(a-b)
    elif oprnd=="*":
        print(a*b)
    elif oprnd=="/":
        print(math.floor(a/b))
    elif oprnd=="?":
        break