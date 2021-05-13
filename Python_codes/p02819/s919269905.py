x=int(input())

if x==2:
    print(2)
    exit()

if x%2==0:x+=1

while True:
    
    k=1

    while True:
        if x%(2*k+1)==0:
            break
        if x**(1/2)<2*k+1:
            print(x)
            exit()

        k+=1
    
    x+=2