x=int(input())

while True:

    i=2
    flag=True
    while i*i<=x:
        if x%i==0:
            flag=False
            break
        i+=1
    
    if flag:
        print(x)
        break
    
    x+=1