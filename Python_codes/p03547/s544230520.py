X,Y=input().split()
XY=[X,Y]
XY.sort()
if X==Y:
    print("=")
elif X==XY[0]:
    print("<")
else:
    print(">")