X,Y = map(str,input().split())
X = int(X,16)
Y = int(Y,16)
if(X < Y):
    print("<")
elif(X > Y):
    print(">")
else:
    print("=")