a,b,c = list(map(int,input().split()))
x = a//c 
y = b//c
if a%c:
    print(y-x)
else:
    print((y-x)+1)