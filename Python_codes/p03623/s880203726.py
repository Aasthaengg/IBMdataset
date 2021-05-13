x,a,b = map(int,input().split())
a1,b1 = abs(x-a),abs(x-b)
if a1 >= b1:
    print("B")
else:
    print("A")
