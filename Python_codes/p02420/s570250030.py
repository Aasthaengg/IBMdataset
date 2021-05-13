while True:
    x=input()
    if x=="-":
        break
    else:
        m=int(input())
        for i in range(int(m)):
            n=int(input())
            y=x[:n]
            x=x+y
            x=x[n:]
    print(x)
