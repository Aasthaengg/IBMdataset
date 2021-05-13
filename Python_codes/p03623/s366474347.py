x,a,b =map(int,input().split())

x1 =abs(x - a)
x2 =abs(x - b)

if x1 > x2:
    print("B")

else:
    print("A")
