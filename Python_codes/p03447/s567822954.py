import sys
x=int(input())
a=int(input())
b=int(input())
x-=a
while(1):
    if x<b:
        print(x)
        sys.exit()
    else:
        x-=b