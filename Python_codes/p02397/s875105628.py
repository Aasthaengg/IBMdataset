while True:
    x=input().split()
    y=[int(x[0]),int(x[1])]
    if y[0]==0 and y[1]==0:
        break
    elif y[0]<y[1]:
        print("{} {}".format(y[0],y[1]))
    elif y[0]>y[1]:
        print("{} {}".format(y[1],y[0]))
    else:
        print("{} {}".format(y[0],y[1]))
