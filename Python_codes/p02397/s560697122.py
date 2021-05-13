while True:
    a = input().split()
    x,y = int(a[0]),int(a[1])
    if x==0 and y==0:
        break
    elif x > y:
        print("%d %d" %(y,x))
    else:
        print("%d %d" %(x,y)) 
        
