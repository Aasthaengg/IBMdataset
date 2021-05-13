X=input()
Y=int(X)
if Y<=99:
    print(0)

else:
    a=10*int(X[-2])+int(X[-1])
    b=a//5
    if a%5!=0:
        b+=1
    if b>Y//100:
        print(0)
    else:
        print(1)