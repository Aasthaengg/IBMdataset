x,y=map(str,input().split())
a=sorted([x,y])
if x==y:
    print("=")
elif x==a[1]:
    print(">")
else:
    print("<")