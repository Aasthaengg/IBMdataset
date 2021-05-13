number=list(map(int,input().split()))
a=number[0]
b=number[1]
c=a*b

key=c%2
if key==0:
    print("Even")
else:
    print("Odd")