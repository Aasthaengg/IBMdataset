k,a,b=map(int,input().split())
if a+1<b:
    if a-1+2>k:
        print(1+k)
    else:
        num1=a-1+2
        num2=b-a
        print(b+((k-num1)//2)*num2+(k-num1)%2)
else:
    print(1+k)
