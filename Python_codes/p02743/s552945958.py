a,b,c=list(map(int,input().split()))
X = c-a-b
if X<0:
    print("No")
else:
    if 4*a*b < X**2:
        print("Yes")
    else:
        print("No")
