k,a,b=map(int,input().split())
if b<a+2:
    print(1+k)
else:
    if k<=a:
        print(1+k)
    else:
        if (k-a-1)%2==0:
            print(b+(b-a)*((k-a-1)//2))
        else:
            print(b+(b-a)*((k-a-1)//2)+1)