n=int(input())
i=1
while i<=n :
    x=i
    if x%3==0  :
        print("",i,end="")
    else:
        if x%10==3 :
            print("",i,end="")
        else :
            while 0<x :
                f=0
                x=x//10
                if x>=1 :
                    if x % 10 ==3 :
                        print("",i,end="")
                        f=1
                if f==1:
                    break
    i=i+1
print("")