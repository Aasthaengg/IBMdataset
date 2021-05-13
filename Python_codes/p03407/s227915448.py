a=input().strip().split(" ")
b=[int(i) for i in a]
Sum=b[0]+b[1]

if(Sum>=b[2]):
    print("Yes")
else:
    print("No")
