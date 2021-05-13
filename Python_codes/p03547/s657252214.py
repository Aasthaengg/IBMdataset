X,Y = map(lambda x:"0x"+x,input().split())
if X > Y:
    print(">")
elif X < Y:
    print("<")
else:
    print("=")