while 1:
    a,b,c = list(map(str,input().split()))
    num_a=int(a)
    num_c=int(c)
    if b=="+":
        print(num_a+num_c)
    elif b=="-":
        print(num_a-num_c)
    elif b=="*":
        print(num_a*num_c)
    elif b=="/":
        print(num_a//num_c)
    elif b=="?":
        break