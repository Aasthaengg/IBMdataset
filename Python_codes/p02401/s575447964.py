while 1:
    x=input().split()
    a=int(x[0])
    op=x[1]
    b=int(x[2])
    if op=='?':
        break
    if op=='+':
        print("%d"%(a+b))
    elif op=='-':
        print("%d"%(a-b))
    elif op=='/':
        print("%d"%(a/b))
    else:
        print("%d"%(a*b))
