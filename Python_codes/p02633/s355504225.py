x=int(input())
if(360%x==0):
    print(int(360/x))
elif(360%(180-x)==0):
    print(int(360/(180-x)))
else:
    m=2
    while(1):
        if((360*m)%x==0):
            print(int(360*m/x))
            break
        elif((360*m)%(180-x)==0):
            print(int(360*m/(180-x)))
            break
        m+=1