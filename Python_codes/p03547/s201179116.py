x,y=input().split()
s=["A","B","C","D","E","F"]
x=s.index(x)
y=s.index(y)

if x<y:
    print("<")
elif x==y:
    print("=")
else:
    print(">")
