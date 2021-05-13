x , a ,b  = map(int,input().split())
X = abs(a - x)
Y = abs(b - x)
Z = min(Y,X)
if Z == X:
    print("A")
else:
    print("B")