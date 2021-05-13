n=int(input())
for i in range(n) :
    if (i+1)%3==0 :
        print(" {}".format(i+1),end="")
    else :
        x=i+1
        while(x!=0) :
            if x%10 == 3 :
                print(" {}".format(i+1),end="")
                break
            x=int(x/10)
print("")
